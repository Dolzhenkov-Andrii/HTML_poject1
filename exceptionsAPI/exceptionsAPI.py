# pylint: disable=C0103
"""_
    Classes for exceptions
"""

from flask_api import status

class APIexception(Exception):
    """
    Base class for all exceptions
    """

class InvalidKey(APIexception):
    """Invalid key in dict
    """
    code = status.HTTP_400_BAD_REQUEST
    message = 'Error getting by key'

class InvalidToken(APIexception):
    """Invalid Token Error
    """
    code = status.HTTP_401_UNAUTHORIZED
    message = 'Request failed due to expiration'

class MissingToken(InvalidKey):
    """Missing Token
    """
    message = 'Request failed due to missing token'

class DecodeToken(MissingToken):
    """Decode Token
    """
    message = 'Request failed due to token error'

class AuthorisationError(MissingToken):
    """Authorisation Error
    """
    message = 'Authorisation Error'

class InvalidLoginOrPassword(AuthorisationError):
    """Wrong login or password
    """
    message = 'wrong login or password'
