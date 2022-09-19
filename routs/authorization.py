"""
    Authorization date
"""
from flask_api import status
from flask import Blueprint, request
from exceptionsAPI import exceptionsAPI
from databases.managers.token_hendler import TokenManager
from validations import Authorization

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
            return exceptionsAPI.InvalidToken.message, exceptionsAPI.InvalidToken.code
        return exceptionsAPI.MissingToken.message, exceptionsAPI.MissingToken.code
    except exceptionsAPI.DecodeToken as error:
        return error.message, error.code


@author.route('/authorization', methods=['POST'])
def authorization():
    """
        Authorization form
    """
    singIn = Authorization(request.get_json()) # pylint: disable=C0103

    try:
        if singIn.valid:
            access = TokenManager.create(SECRET_KEY, ACCESS_TOKEN_TIME, 'ID_USER')
            refresh = TokenManager.create(SECRET_KEY, REFRESH_TOKEN_TIME, 'ID_USER')
            return {'access_token': access,
                    'refresh_token': refresh,
                    'user': singIn.user}, status.HTTP_200_OK
        raise exceptionsAPI.InvalidLoginOrPassword
    except exceptionsAPI.DecodeToken as error:
        return error.message, error.code
    except exceptionsAPI.AuthorisationError as error:
        return error.message, error.code
