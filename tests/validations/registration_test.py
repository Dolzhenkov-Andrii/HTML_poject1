"""
    Test Registration validator
"""
from unittest import TestCase
from dateutil import parser
from exceptions.basic import APIexception
from exceptions.validate import ErrorAuthorisation
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
    'password': TEST_USER_PASSWORD,
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

    def test_success_check(self):
        """
            Test for user registration form validation
        """
        test_form = Registration(**test_request_data)
        valid_request_data = test_form.validate()

        self.assertEqual(valid_request_data['birthday'], parser.parse(
            test_request_data['birthday']))
        self.assertEqual(
            valid_request_data['username'], test_request_data['username'])
        self.assertEqual(
            valid_request_data['password'], test_request_data['password'])
        self.assertEqual(
            valid_request_data['email'], test_request_data['email'])
        self.assertEqual(
            valid_request_data['surname'], test_request_data['surname'])
        self.assertEqual(valid_request_data['name'], test_request_data['name'])
        self.assertEqual(
            valid_request_data['phone'], test_request_data['phone'])

    def test_missing_fields_in_the_form(self):
        """
            checking for error "1" when the field is missing in the registration form
        """
        invalid_request_data = {
            'username': TEST_USER_USERNAME,
            'pasword': TEST_USER_PASSWORD,
            'email': TEST_USER_EMAIL,
            'surname': TEST_USER_SURNAME,
            'name': TEST_USER_NAME,
        }
        test_form = Registration(**invalid_request_data)
        try:
            test_form.validate()
        except APIexception as error:
            self.assertEqual(error.message, ErrorAuthorisation.message)

    def test_missing_registration_form(self):
        """
            checking for error "1" when the field is missing in the registration form
        """
        test_form = Registration(**{})
        try:
            test_form.validate()
        except APIexception as error:
            self.assertEqual(error.message, ErrorAuthorisation.message)
