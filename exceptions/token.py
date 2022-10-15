"""_
    Tokens exceptions
"""
from exceptions.basic import APIexception


class DecodeToken(APIexception):
    """Decode Token
    """
    message = 'Request failed due to token error'

class ExpirationToken(DecodeToken):
    """Invalid Token Error
    """
    message = 'Request failed due to expiration'

class InvalidToken(DecodeToken):
    """Invalid Token Error
    """
    message = 'Request failed due to token error'

class MissingToken(DecodeToken):
    """Missing Token
    """
    message = 'Request failed due to missing token'
