'''Routs UpdateUser
'''

from exceptions.validate import APIexception, ErrorForms
from validations.checking_db_fields import (
    valid_field
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
        self.validate_request_data = {}


    def validate(self):
        '''Key verification
        '''

        try:
            for key in UpdateUser.validate_fields: # pylint: disable=C0206
                if (key not in self.request_data
                    or isinstance(self.request_data[key],
                                  UpdateUser.validate_fields[key]) is False):
                    raise ErrorForms

                if self.request_data[key]:
                    self.validate_request_data[key] = valid_field(
                        data=self.request_data[key],
                        key=key
                        )
                else:
                    self.validate_request_data[key] = None
        except APIexception as error:
            raise error
        return self.validate_request_data
