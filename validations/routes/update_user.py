'''Routs UpdateUser
'''

from exceptions.validate import ErrorForms
from validations.checking_db_fields import (
    valid_surname_field,
    valid_name_field,
    valid_birthday_field,
    valid_phone_field,
)


class UpdateUser:
    '''Registration check
    '''
    validate_fields = {
        'surname': str,
        'name': str,
        'birthday': str,
        'phone': str,
    }

    def __init__(self, **request_data):
        self.request_data = request_data


    def validate(self):
        '''Key verification
        '''
        for key in UpdateUser.validate_fields:  # pylint: disable=C0206
            if (key not in self.request_data
                    or isinstance(self.request_data[key],
                                  UpdateUser.validate_fields[key]) is False):
                raise ErrorForms
        try:
            validate_request_data = {
                'surname': valid_surname_field(self.request_data['surname']),
                'name': valid_name_field(self.request_data['name']),
                'birthday': valid_birthday_field(self.request_data['birthday']),
                'phone': valid_phone_field(self.request_data['phone']),
            }
        except ErrorForms as error:
            raise error
        return validate_request_data
