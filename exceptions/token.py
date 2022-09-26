"""_
    Tokens exceptions
"""
from exceptions.basic import APIexception


class DecodeToken(APIexception):
    """Decode Token
    """
    message = 'Request failed due to token error'

class InvalidToken(APIexception):
    """Invalid Token Error
    """
    message = 'Request failed due to expiration'

class MissingToken(APIexception):
    """Missing Token
    """
    message = 'Request failed due to missing token'
