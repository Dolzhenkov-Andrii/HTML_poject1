"""Routs validations
"""
# from flask_api import status

from exceptions.validate import ErrorAuthorisation

class Authorization:
    """Authorization check
    """
    validate_fields = {
        'username': str,
        'password': str,
        'remember_me': bool,
    }

    def __init__(self, **request_data):
        self.request_data = request_data

    def validate(self):
        """Key verification
        """
        for key in Authorization.validate_fields: # pylint: disable=C0206
            if (key not in self.request_data
                or isinstance(self.request_data[key], Authorization.validate_fields[key]) is False):
                raise ErrorAuthorisation
        return self.request_data
