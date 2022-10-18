"""Routs validations
"""

from validations.string_valid import valid_string_characters, valid_string_size
from exceptions.validate import ErrorAuthorisation, InvalidString
from config.config import (
    VALID_MAX_SIZE_PASSWORD,
    VALID_MIN_SIZE_PASSWORD,
    VALID_MAX_SIZE_USERNAME,
    VALID_MIN_SIZE_USERNAME,
)


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
        for key in Authorization.validate_fields:  # pylint: disable=C0206
            if (key not in self.request_data
                    or isinstance(self.request_data[key],
                                  Authorization.validate_fields[key]) is False):
                raise ErrorAuthorisation

    def validate(self):
        """Key verification
        """
        try:
            valid_string_size(
                string=self.request_data['username'],
                min_size=VALID_MIN_SIZE_USERNAME,
                max_size=VALID_MAX_SIZE_USERNAME
            )
        except InvalidString as error:
            error.message = f'{error.message} in "Username"'
            raise error

        try:
            valid_string_characters(
                string=self.request_data['username'], characters="^[a-zA-Z0-9_-]+$")
        except InvalidString as error:
            error.message = f'{error.message} "Username"'
            raise error

        try:
            valid_string_size(
                string=self.request_data['password'],
                min_size=VALID_MIN_SIZE_PASSWORD,
                max_size=VALID_MAX_SIZE_PASSWORD
            )
        except InvalidString as error:
            error.message = f'{error.message} in "Password"'
            raise error

        return self.request_data
