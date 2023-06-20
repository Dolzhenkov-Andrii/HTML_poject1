'''
    Registrations and activations routes for User
'''
from hashlib import pbkdf2_hmac
from flask_api import status
from flask import Blueprint, request
from config.db import db
from config.config import (
    ACTIVE_USER_STATUS,
    NOT_ACTIVE_USER_STATUS,
    PASSWORD_SALT,
    REFRESH_REMEMBER_TOKEN_TIME,
    SECRET_KEY,
    ACCESS_TOKEN_TIME,
)

from databases.models.userStatus import UserStatus
from databases.models.user import User
from databases.models.activation_key import ActivationKey

from tokens.token_hendler import TokenManager
from service.email_messange import activate_email
from validations.routes.registration import Registration
from validations.routes.authorization import Authorization
from exceptions.token import InvalidToken, MissingToken, ExpirationToken, DecodeToken
from exceptions.validate import InvalidString, ErrorForms, InvalidAuthorisation

registration = Blueprint('registeration', __name__,
                         template_folder='templates')


@registration.route('/new-user', methods=['POST'])
def set_registration():
    '''
        New user
    '''
    try:
        registr_form = Registration(**request.form)
        validated_data = registr_form.validate()
    except ErrorForms as error:
        return error.message, status.HTTP_400_BAD_REQUEST
    except InvalidString as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    if_username = User.query.filter_by(
        username=validated_data['username']).first()
    if if_username:
        return 'There is already a user with the same username', status.HTTP_400_BAD_REQUEST

    if_user_email = User.query.filter_by(
        email=validated_data['email']).first()
    if if_user_email:
        return 'There is already a user with this email address', status.HTTP_400_BAD_REQUEST

    user_status = UserStatus.query.filter_by(
        name=NOT_ACTIVE_USER_STATUS).first()
    if user_status is None:
        user_status = UserStatus()
        user_status.name = NOT_ACTIVE_USER_STATUS
        db.session.add(user_status)  # pylint: disable=no-member
        db.session.commit()  # pylint: disable=no-member
    # Test user
    new_user = User()
    pasword = pbkdf2_hmac('sha256',
                          validated_data['password'].encode('utf-8'),
                          PASSWORD_SALT.encode('utf-8'),
                          100000)
    new_user.pasword = pasword.hex()
    new_user.username = validated_data['username']
    new_user.email = validated_data['email']
    new_user.status_id = UserStatus.query.filter_by(
        name=NOT_ACTIVE_USER_STATUS).first().id
    db.session.add(new_user)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member
    user_in_db = User.query.filter_by(
        username=validated_data['username']).first()

    hash_key = TokenManager.create(
        SECRET_KEY, REFRESH_REMEMBER_TOKEN_TIME, {'user_id': user_in_db.id, })
    activ_key = ActivationKey()
    activ_key.hash_key = hash_key
    activ_key.user_id = user_in_db.id
    db.session.add(activ_key)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member

    try:
        activate_email(user_in_db.email, user_in_db.username, hash_key)
    except IOError as err:
        return err.strerror, status.HTTP_500_INTERNAL_SERVER_ERROR

    return {
        'username': user_in_db.username,
        'email': user_in_db.email,
    }, status.HTTP_200_OK


@registration.route('/account-activation', methods=['GET'])
def get_activation():
    '''
        Activation user email
    '''
    activation_key = request.args.get('activation', default=None, type=str)

    if not activation_key is None:
        try:
            if TokenManager.valid(SECRET_KEY, activation_key):
                valid_activ_key = ActivationKey.query.filter_by(
                    hash_key=activation_key).first()
                if not valid_activ_key is None:
                    user = User.query.filter_by(
                        id=valid_activ_key.user_id).first()

                    user_status = UserStatus.query.filter_by(
                        name=ACTIVE_USER_STATUS).first()
                    if user_status is None:
                        user_status = UserStatus()
                        user_status.name = ACTIVE_USER_STATUS
                        db.session.add(user_status)  # pylint: disable=no-member
                        db.session.commit()  # pylint: disable=no-member

                    user.status_id = UserStatus.query.filter_by(
                        name=ACTIVE_USER_STATUS).first().id
                    db.session.add(user)  # pylint: disable=no-member
                    db.session.commit()  # pylint: disable=no-member

                    access = TokenManager.create(
                        SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': valid_activ_key.user_id, })
                    refresh = TokenManager.create(SECRET_KEY,
                                                  REFRESH_REMEMBER_TOKEN_TIME,
                                                  {'user_id': valid_activ_key.user_id,
                                                   'remember': True}
                                                  )
                    return {'access_token': access,
                            'refresh_token': refresh,
                            'user': user,
                            }, status.HTTP_200_OK

        except ExpirationToken as error:
            return error.message, status.HTTP_400_BAD_REQUEST
        except InvalidToken as error:
            return error.message, status.HTTP_400_BAD_REQUEST
    return MissingToken.message, status.HTTP_400_BAD_REQUEST


@registration.route('/account-reactivation', methods=['POST'])
def set_reactivation():
    '''
        Account Reactivation If the key has expired
    '''
    try:
        sing_in = Authorization(**request.get_json())
        validated_data = sing_in.validate()
    except ErrorForms as error:
        return error.message, status.HTTP_400_BAD_REQUEST
    except InvalidString as error:
        return error.message, status.HTTP_400_BAD_REQUEST
    try:
        user = User.query.filter_by(username=validated_data['username']).first()
        hash_key = pbkdf2_hmac('sha256', validated_data['password'].encode(
                'utf-8'), PASSWORD_SALT.encode('utf-8'), 100000)
        if user is None or (user.pasword == hash_key.hex()) is False:
            return InvalidAuthorisation.message, status.HTTP_401_UNAUTHORIZED

        hash_key = TokenManager.create(
            SECRET_KEY, REFRESH_REMEMBER_TOKEN_TIME, {'user_id': user.id, })
        activ_key = ActivationKey()
        activ_key.hash_key = hash_key
        activ_key.user_id = user.id
        db.session.add(activ_key)  # pylint: disable=no-member
        db.session.commit()  # pylint: disable=no-member

        activate_email(user.email, user.username, hash_key)

        return {
            'username': user.username,
            'email': user.email,
        }, status.HTTP_200_OK
    except IOError as err:
        return err.strerror, status.HTTP_500_INTERNAL_SERVER_ERROR
    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST
