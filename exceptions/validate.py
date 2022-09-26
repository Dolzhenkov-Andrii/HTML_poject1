"""_
    Classes for exceptions
"""
from exceptions.basic import APIexception

class InvalidKey(APIexception):
    """Invalid key in dict
    """
    message = 'Error getting by key'

class ErrorAuthorisation(APIexception):
    """Authorisation Error
    """
    message = 'Authorisation Error'

class InvalidAuthorisation(APIexception):
    """Wrong login or password
    """
    message = 'Wrong login or password'
