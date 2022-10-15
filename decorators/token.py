"""
    Decorators
"""
from flask_api import status
from flask import request
from config.config import SECRET_KEY
from tokens.token_hendler import TokenManager
from exceptions.token import DecodeToken, MissingToken, InvalidToken


def token_required(func):
    """Token_required

    Args:
        func (@app.route): Checks for tokens and their renewal
    """

    def decorated(*args, **kwargs):
        if 'Access-Token' in dict(request.headers):
            try:
                TokenManager.valid(SECRET_KEY, request.headers['Access-Token'])
                return func(*args, **kwargs)
            except InvalidToken as error:
                return error.message, status.HTTP_400_BAD_REQUEST
            except DecodeToken as error:
                return error.message, status.HTTP_401_UNAUTHORIZED
        return MissingToken.message, status.HTTP_401_UNAUTHORIZED
    return decorated
