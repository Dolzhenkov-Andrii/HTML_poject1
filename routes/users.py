'''
    User rout
'''

from flask_api import status
from flask import Blueprint, request
from decorators.token import token_required
from config.db import db
from config.config import SECRET_KEY

from service.upload_image import UploadImage
from databases.models.user import User
from databases.models.photo import Photo
from tokens.token_hendler import TokenManager
from validations.routes.update_user import UpdateUser

from exceptions.validate import ErrorForms, InvalidImage
from exceptions.token import DecodeToken

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/user/update', methods=['POST', 'GET'])
@token_required
def update_user():
    '''
        Update user informations
    '''

    try:
        update_form = UpdateUser(**request.form)
        validated_data = update_form.validate()
    except ErrorForms as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    try:
        user_id = TokenManager.get_id_user(SECRET_KEY ,request.headers['Access-Token'])
    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    avatar_name = None
    if request.method == 'POST' and 'file' in request.files:
        try:
            avatar_name = UploadImage(request.files['file']).save_image()
        except InvalidImage as error:
            return error.message, status.HTTP_400_BAD_REQUEST

    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        if avatar_name is not None:
            avatar = Photo()
            avatar.photo = avatar_name
            avatar.user_id = user.id
            db.session.add(avatar)  # pylint: disable=no-member
            db.session.commit()  # pylint: disable=no-member
            user.photo = avatar_name
        user.surname = validated_data.get('surname')
        user.name = validated_data.get('name')
        user.phone = validated_data.get('phone')
        user.birthday = validated_data.get('birthday')
        db.session.commit() # pylint: disable=no-member
        return {'user': user}, status.HTTP_200_OK
    return 'Error: "User is not found..."', status.HTTP_400_BAD_REQUEST
