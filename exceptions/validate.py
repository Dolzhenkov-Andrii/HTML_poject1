"""_
    Classes for exceptions
"""
from exceptions.basic import APIexception, InvalidString

class InvalidKey(APIexception):
    """Invalid key in dict
    """
    message = 'Error getting by key'

class ErrorAuthorisation(InvalidString):
    """Authorisation Error
    """
    message = 'Authorisation Error'

class InvalidAuthorisation(ErrorAuthorisation):
    """Wrong login or password
    """
    message = 'Wrong login or password'

class InvalidStringMaxSize(InvalidString):
    """invalid string max size
    """
    message = 'Invalid string max size'

class InvalidStringMinSize(InvalidString):
    """invalid string min size
    """
    message = 'Invalid string min size'

class InvalidCharactersInString(InvalidString):
    """invalid characters in string
    """
    message = 'Invalid characters in string'
