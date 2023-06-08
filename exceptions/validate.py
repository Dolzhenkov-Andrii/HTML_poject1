"""_
    Classes for exceptions
"""
from dateutil.parser._parser import ParserError
from email_validator import EmailNotValidError
from exceptions.basic import APIexception, InvalidString

class InvalidKey(APIexception):
    """Invalid key in dict
    """
    message = 'Error getting by key'

class InvalidType(APIexception):
    """Invalid key in dict
    """
    message = 'Invalid type'

class ErrorForms(APIexception):
    """Authorisation Error
    """
    message = 'Forms Error'

class InvalidAuthorisation(ErrorForms):
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

class InvalidEmail(EmailNotValidError):
    """invalid email address
    """
    message = 'Wrong email address'

class InvalidDate(ParserError):
    """invalid date
    """
    message = 'Invalid date format'

class InvalidImage(APIexception):
    """ invalid image
    """
    message = 'Invalid Image'

class InvalidImageFormat(InvalidImage):
    """ invalid image
    """
    message = 'Invalid Image Format'
