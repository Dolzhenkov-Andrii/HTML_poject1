"""Routs registration
"""

from exceptions.validate import ErrorAuthorisation
from validations.checking_db_fields import (
    valid_username_field,
    valid_pasword_field,
    valid_email_field,
    valid_surname_field,
    valid_name_field,
    valid_birthday_field,
    valid_phone_field,
)


class Registration:
    """Registration check
    """
    validate_fields = {
        'username': str,
        'password': str,
        'email': str,
        'surname': str,
        'name': str,
        'birthday': str,
        'phone': str,
    }

    def __init__(self, **request_data):
        self.request_data = request_data


    def validate(self):
        """Key verification
        """
        for key in Registration.validate_fields:  # pylint: disable=C0206
            if (key not in self.request_data
                    or isinstance(self.request_data[key],
                                  Registration.validate_fields[key]) is False):
                raise ErrorAuthorisation
        try:
            validate_request_data = {
                'username': valid_username_field(self.request_data['username']),
                'password': valid_pasword_field(self.request_data['password']),
                'email': valid_email_field(self.request_data['email']),
                'surname': valid_surname_field(self.request_data['surname']),
                'name': valid_name_field(self.request_data['name']),
                'birthday': valid_birthday_field(self.request_data['birthday']),
                'phone': valid_phone_field(self.request_data['phone']),
            }
        except Exception as error:
            raise error
        return validate_request_data
