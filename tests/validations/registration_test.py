"""
    Test Registration validator
"""
from unittest import TestCase
from validations.routes.registration import Registration
from config.config import (
    TEST_USER_USERNAME,
    TEST_USER_PASSWORD,
    TEST_USER_SURNAME,
    TEST_USER_NAME,
    TEST_USER_EMAIL,
    TEST_USER_BIRTHDAY,
    TEST_USER_PHONE,
)

test_request_data = {
            'username': TEST_USER_USERNAME,
            'pasword': TEST_USER_PASSWORD,
            'email': TEST_USER_EMAIL,
            'surname': TEST_USER_SURNAME,
            'name': TEST_USER_NAME,
            'birthday': TEST_USER_BIRTHDAY,
            'phone': TEST_USER_PHONE,
        }

class RegistrationValidTest(TestCase):
    """
        A test that checks the correct operation
        of the registration validator.
    """

    def test_for_work(self):
        """Test 1"""
        test_form = Registration(**test_request_data)
        try:
           valid_request_data = test_form.validate()
        except Exception as error:
            self.assertEqual(error.message, 'Error')
        self.assertEqual(valid_request_data, dict)
