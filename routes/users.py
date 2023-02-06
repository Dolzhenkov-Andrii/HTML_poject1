'''
    User rout
'''

from flask_api import status
from flask import Blueprint, request
from config.db import db
from config.config import SECRET_KEY
from databases.models.user import User
from tokens.token_hendler import TokenManager
from decorators.token import token_required
from validations.routes.update_user import UpdateUser
from exceptions.validate import ErrorForms, InvalidString
from exceptions.token import DecodeToken


users = Blueprint('users', __name__, template_folder='templates')


@users.route('/user/update', methods=['POST'])
@token_required
def update_user():
    '''
        Update user informations
    '''

    try:
        update_form = UpdateUser(**request.get_json())
        validated_data = update_form.validate()
    except ErrorForms as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    try:
        user_id = TokenManager.get_id_user(SECRET_KEY ,request.headers['Access-Token'])
    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    user = User.query.filter_by(id=user_id).first()

    if user is not None:
        user.surname = validated_data['surname']
        user.name = validated_data['name']
        user.phone = validated_data['phone']
        user.birthday = validated_data['birthday']
        db.session.commit() # pylint: disable=no-member
        return {'user': user}, status.HTTP_200_OK
    return 'Error: "User is not found..."', status.HTTP_400_BAD_REQUEST
