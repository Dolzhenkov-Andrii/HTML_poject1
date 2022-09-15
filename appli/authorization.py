"""
    Authorization date
"""
import hashlib
from flask import Blueprint, request
from databases.models.user import User
from databases.managers.token_hendler import create_token, valid_token
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
            if valid_token(SECRET_KEY, request.headers['refresh_token']) is False:
                return {'code': 17010, 'message': 'Error: Signature has expired'}
        else:
            return {'code': 17011, 'message': 'Error: getting token'}
        # access_token = TokenManager.create(SECRET_KEY, ACCESS_TOKEN_TIME, 'ID_USER')
        access = create_token(SECRET_KEY, ACCESS_TOKEN_TIME, 'ID_USER')
        refresh = create_token(SECRET_KEY, REFRESH_TOKEN_TIME, 'ID_USER')
        return {'code': 200, 'access_token': access, 'refresh_token': refresh}
    except TypeError:  # <- Не знаю какой ставить...
        return {'code': 17012, 'message': 'Error valid token'}


@author.route('/authorization', methods=['POST'])
def authorization():
    """
        Authorization form
    """
    # Переделать!!!!!!!==================
    autho_Form = request.get_json() # pylint: disable=C0103
    login = autho_Form['login']
    password = autho_Form['password']
    # ===================================

    hashed = hashlib.md5(password.encode())
    try:
        user = User.query.filter_by(username=f'{login}').first()
        if user is None:
            return {'code': 402, 'message': 'Error1: Login or Password'}
        elif user.pasword != hashed.hexdigest():
            return {'code': 402, 'message': 'Error2: Login or Password'}
        access = create_token(SECRET_KEY, ACCESS_TOKEN_TIME, 'ID_USER')
        refresh = create_token(SECRET_KEY, REFRESH_TOKEN_TIME, 'ID_USER')
        return {'code': 200,
                'access_token': access,
                'refresh_token': refresh,
                'user': user,
                'request': hashed.hexdigest()}
    except TypeError:
        return {'code': 400, 'message': 'Error3: Login or Password'}
