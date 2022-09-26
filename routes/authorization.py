"""
    Authorization date
"""
from hashlib import pbkdf2_hmac
from flask_api import status
from flask import Blueprint, request
from exceptions.token import InvalidToken, MissingToken, DecodeToken
from exceptions.validate import InvalidAuthorisation
from databases.models.user import User
from tokens.token_hendler import TokenManager
from validations.validations import Authorization

from config.config import SECRET_KEY, ACCESS_TOKEN_TIME, REFRESH_TOKEN_TIME

author = Blueprint('author', __name__, template_folder='templates')


@author.route('/refresh_token')
def refresh_token():
    """Update token

    Returns:
        json: new tokens
    """
    try:
        if 'Refresh-Token' in dict(request.headers):
            if TokenManager.valid(SECRET_KEY, request.headers['refresh_token']):
                #Поміркувати що замість ID_USER передавати
                access = TokenManager.create(SECRET_KEY, ACCESS_TOKEN_TIME, 'ID_USER')
                refresh = TokenManager.create(SECRET_KEY, REFRESH_TOKEN_TIME, 'ID_USER')
                return {'access_token': access, 'refresh_token': refresh}, status.HTTP_200_OK
            return InvalidToken.message, status.HTTP_400_BAD_REQUEST
        return MissingToken.message, status.HTTP_400_BAD_REQUEST
    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST


@author.route('/authorization', methods=['POST'])
def authorization():
    """
        Authorization form
    """
    try:
        sing_in = Authorization(**request.get_json())
        validated_data = sing_in.validate()
    except MissingToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    try:
        user = User.query.filter_by(username=f"{validated_data['username']}").first()
        hash_key = pbkdf2_hmac('sha256',
                                validated_data['password'].encode('utf-8'),
                                b'YtnCjkbD#$%Cfkfnf['*2,
                                100000)
        if user is None or (user.pasword == hash_key.hex()) is False:
            return InvalidAuthorisation.message, status.HTTP_400_BAD_REQUEST

        access = TokenManager.create(SECRET_KEY, ACCESS_TOKEN_TIME, 'ID_USER')
        refresh = TokenManager.create(SECRET_KEY, REFRESH_TOKEN_TIME, 'ID_USER')
        return {'access_token': access,
                'refresh_token': refresh,
                'user': user}, status.HTTP_200_OK
    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST
