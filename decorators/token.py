"""
    Decorators
"""
from flask_api import status
from flask import request
from config.config import SECRET_KEY
from tokens.token_hendler import TokenManager
from exceptions.token import InvalidToken, DecodeToken
# from databases.managers.json_valid import request_data

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
            except DecodeToken:
                return InvalidToken.message, status.HTTP_400_BAD_REQUEST
        return InvalidToken.message, status.HTTP_400_BAD_REQUEST
    return decorated
