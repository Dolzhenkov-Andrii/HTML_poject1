"""
    Decorators
"""

from flask import request
from config.config import SECRET_KEY
from databases.managers.token_hendler import TokenManager
from exceptionsAPI.exceptionsAPI import InvalidToken, MissingToken

def token_required(func):
    """Token_required

    Args:
        func (@app.route): Checks for tokens and their renewal
    """
    def decorated(*args, **kwargs):
        if 'Access-Token' in dict(request.headers):
            if TokenManager.valid(SECRET_KEY, request.headers['access_token']):
                return func(*args, **kwargs)
            return InvalidToken.message, InvalidToken.code
        return MissingToken.message, MissingToken.code
    return decorated
