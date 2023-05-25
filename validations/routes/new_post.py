'''Routs validations
'''


from exceptions.validate import ErrorForms, InvalidString
from validations.string_valid import valid_string_size
from config.config import (
    VALID_MAX_SIZE_POST_TEXT,
    VALID_MAX_SIZE_POST_TITLE,
    VALID_MIN_SIZE_POST_TEXT,
    VALID_MIN_SIZE_POST_TITLE,
)

class PostValid:
    '''Authorization check
    '''
    validate_fields = {
        'title': str,
        'text': str,
    }

    def __init__(self, **request_data):
        self.request_data = request_data


    def validate(self):
        '''Key verification
        '''
        for key in PostValid.validate_fields:  # pylint: disable=C0206
            if (key not in self.request_data
                    or isinstance(self.request_data[key],
                                  PostValid.validate_fields[key]) is False):
                raise ErrorForms
        try:
            validate_request_data = {
                'title': valid_string_size(self.request_data['title'],
                                           max_size=VALID_MAX_SIZE_POST_TITLE,
                                           min_size=VALID_MIN_SIZE_POST_TITLE),
                'text': valid_string_size(self.request_data['text'],
                                           max_size=VALID_MAX_SIZE_POST_TEXT,
                                           min_size=VALID_MIN_SIZE_POST_TEXT),
            }
        except InvalidString as error:
            raise error
        return validate_request_data
