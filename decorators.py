"""
    Decorators
"""
from flask import request
from config.config import SECRET_KEY
from databases.managers.token_hendler import valid_token
# from databases.managers.token_hendler import TokenManager

def token_required(func):
    """Token_required

    Args:
        func (@app.route): Checks for tokens and their renewal
    """
    def decorated(*args, **kwargs):
        try:
            if 'Access-Token' in dict(request.headers):
                if valid_token(SECRET_KEY, request.headers['access_token']) is False:
                    return {'code': 17010, 'message': 'Error: Signature has expired'}
            return func(*args, **kwargs)
        except TypeError: # <- Не знаю какой ставить...
            return func(*args, {'kwargs':kwargs,
                                'code': 17012,
                                'message': 'Error: Valid token'})
    return decorated
