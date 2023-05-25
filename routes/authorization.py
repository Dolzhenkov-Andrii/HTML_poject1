'''
    Authorization date
'''
from hashlib import pbkdf2_hmac
from flask_api import status
from flask import Blueprint, request
from config.db import db
from config.config import (
    ACCESS_TOKEN_TIME,
    REFRESH_TOKEN_TIME,
    REFRESH_REMEMBER_TOKEN_TIME,
    PASSWORD_SALT,
    SECRET_KEY,
    NOT_ACTIVE_USER_STATUS,
)
from exceptions.token import InvalidToken, DecodeToken, MissingToken, ExpirationToken
from exceptions.validate import (
    InvalidAuthorisation,
    InvalidString,
    ErrorForms,
    InvalidEmail,
    InvalidCharactersInString
)
from databases.models.user import User
from databases.models.activation_key import ActivationKey
from tokens.token_hendler import TokenManager
from validations.routes.authorization import Authorization
from validations.checking_db_fields import valid_email_field, valid_username_field
from service.email_messange import password_recovery

author = Blueprint('author', __name__, template_folder='templates')


@author.route('/refresh_token')
def refresh_token():
    '''Update token

    Returns:
        json: new tokens
    '''
    try:
        if ('Refresh-Token' in dict(request.headers)
            and TokenManager.valid(SECRET_KEY,
                                   request.headers['refresh_token'])):

            remember = TokenManager.token_data(
                SECRET_KEY, request.headers['refresh_token'])

            token_time = REFRESH_TOKEN_TIME
            if remember['remember']:
                token_time = REFRESH_REMEMBER_TOKEN_TIME

            access = TokenManager.create(
                SECRET_KEY, ACCESS_TOKEN_TIME, data={'user_id': remember['user_id'], })
            refresh = TokenManager.create(
                SECRET_KEY, token_time, remember)

            return {'access_token': access, 'refresh_token': refresh}, status.HTTP_200_OK

        return MissingToken.message, status.HTTP_400_BAD_REQUEST
    except ExpirationToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST
    except InvalidToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST


@author.route('/authorization', methods=['POST'])
def authorization():
    '''
        Authorization form
    '''
    try:
        sing_in = Authorization(**request.get_json())
        validated_data = sing_in.validate()
    except ErrorForms as error:
        return error.message, status.HTTP_400_BAD_REQUEST
    except InvalidString as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    try:
        user = User.query.filter_by(
            username=f"{validated_data['username']}").first()
        hash_key = pbkdf2_hmac('sha256', validated_data['password'].encode(
            'utf-8'), PASSWORD_SALT.encode('utf-8'), 100000)

        if user.status.name == NOT_ACTIVE_USER_STATUS:
            return 'Account not activated', status.HTTP_401_UNAUTHORIZED

        if user is None or (user.pasword == hash_key.hex()) is False:
            return InvalidAuthorisation.message, status.HTTP_401_UNAUTHORIZED

        token_time = REFRESH_TOKEN_TIME
        if validated_data['remember_me']:
            token_time = REFRESH_REMEMBER_TOKEN_TIME

        access = TokenManager.create(
            SECRET_KEY, ACCESS_TOKEN_TIME, data={'user_id': user.id, })
        refresh = TokenManager.create(SECRET_KEY, token_time, {'user_id': user.id,
                                      'remember': validated_data['remember_me']})

        return {'access_token': access,
                'refresh_token': refresh,
                'user': user, }, status.HTTP_200_OK

    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST


@author.route('/password-recovery', methods=['POST'])
def set_password_recovery():
    '''
        Password recovery
    '''
    email = request.args.get('email', default=None, type=str)
    username = request.args.get('username', default=None, type=str)
    if email is None and username is None:
        return 'Missing email or username', status.HTTP_400_BAD_REQUEST

    if email:
        try:
            valid_email = valid_email_field(email)
        except InvalidEmail as err:
            return err.message, status.HTTP_400_BAD_REQUEST

        user = User.query.filter_by(email=valid_email).first()
        if user is None:
            return 'No user with this email address', status.HTTP_404_NOT_FOUND
    elif username:
        try:
            valid_username = valid_username_field(username)
        except InvalidCharactersInString as err:
            return err.message, status.HTTP_400_BAD_REQUEST

        user = User.query.filter_by(username=valid_username).first()
        if user is None:
            return 'No user with this username', status.HTTP_404_NOT_FOUND

    if user.status.name == NOT_ACTIVE_USER_STATUS:
            return 'Account not activated', status.HTTP_401_UNAUTHORIZED

    hash_key = TokenManager.create(
        SECRET_KEY, REFRESH_REMEMBER_TOKEN_TIME, {'user_id': user.id, })
    activ_key = ActivationKey()
    activ_key.hash_key = hash_key
    activ_key.user_id = user.id
    db.session.add(activ_key)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member

    password_recovery(user.email, user.username, hash_key)

    return {
        'username': user.username,
        'email': user.email,
    }, status.HTTP_200_OK


@author.route('/new-password', methods=['POST'])
def get_activation():
    '''
        Changes the user's password
    '''
    try:
        user_form = Authorization(**request.get_json())
        validated_data = user_form.validate()
    except ErrorForms as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    hash_key = request.args.get('hash_key', default=None, type=str)

    if not hash_key is None:
        try:
            if TokenManager.valid(SECRET_KEY, hash_key):
                valid_hash_key = ActivationKey.query.filter_by(
                    hash_key=valid_hash_key).first()
                if not valid_hash_key is None:
                    user = User.query.filter_by(
                        id=valid_hash_key.user_id).first()
                    if validated_data['username'] == user.username:
                        hash_password_key = pbkdf2_hmac('sha256', validated_data['password'].encode(
                            'utf-8'), PASSWORD_SALT.encode('utf-8'), 100000)
                        user.pasword = hash_password_key
                        db.session.add(user)  # pylint: disable=no-member
                        db.session.commit()  # pylint: disable=no-member
                        access = TokenManager.create(
                            SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': valid_hash_key.user_id, })
                        refresh = TokenManager.create(SECRET_KEY,
                                                      REFRESH_REMEMBER_TOKEN_TIME,
                                                      {'user_id': valid_hash_key.user_id,
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
