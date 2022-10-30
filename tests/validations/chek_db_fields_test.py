"""
    Test functions for cheking databases fields
"""
from unittest import TestCase
from dateutil import parser
from exceptions.validate import (
    InvalidString,
    InvalidStringMinSize,
    InvalidStringMaxSize,
    InvalidCharactersInString,
    InvalidDate,
    InvalidEmail,
    InvalidType,
)
from validations.checking_db_fields import (
    valid_username_field,
    valid_pasword_field,
    valid_email_field,
    valid_surname_field,
    valid_name_field,
    valid_birthday_field,
    valid_phone_field,
)
from config.config import (
    TEST_USER_USERNAME,
    TEST_USER_PASSWORD,
    TEST_USER_SURNAME,
    TEST_USER_NAME,
    TEST_USER_EMAIL,
    TEST_USER_BIRTHDAY,
    TEST_USER_PHONE,
)


class ValidUsernameFieldTest(TestCase):
    """
        Check for invalid 'username'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_username = valid_username_field(TEST_USER_USERNAME)
        self.assertEqual(valid_username, TEST_USER_USERNAME)

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_username = None
        invalid_username = True
        try:
            not_return_username = valid_email_field(invalid_username)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_username, None)

    def test_error_min_size(self):
        """
            Test for raise error: InvalidStringMinSize
        """
        not_return_username = None
        invalid_username = 'Yan'
        try:
            not_return_username = valid_username_field(invalid_username)
        except InvalidString as error:
            self.assertIn(InvalidStringMinSize.message, error.message)
        self.assertEqual(not_return_username, None)

    def test_error_max_size(self):
        """
            Test for raise error: InvalidStringMaxSize
        """
        not_return_username = None
        invalid_username = 'Yan'*30
        try:
            not_return_username = valid_username_field(invalid_username)
        except InvalidString as error:
            self.assertIn(InvalidStringMaxSize.message, error.message)
        self.assertEqual(not_return_username, None)

    def test_error_characters(self):
        """
            Test for raise error: InvalidCharactersInString
        """
        not_return_username = None
        invalid_username = 'UserTest@#$'
        try:
            not_return_username = valid_username_field(invalid_username)
        except InvalidString as error:
            self.assertIn(InvalidCharactersInString.message, error.message)
        self.assertEqual(not_return_username, None)


class ValidPaswordFieldTest(TestCase):
    """
        Check for invalid 'password'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_password = valid_pasword_field(TEST_USER_PASSWORD)
        self.assertEqual(valid_password, TEST_USER_PASSWORD)

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_password = None
        invalid_password = 3145697463
        try:
            not_return_password = valid_email_field(invalid_password)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_password, None)

    def test_error_min_size(self):
        """
            Test for raise error: InvalidStringMinSize
        """
        not_return_password = None
        invalid_password = 'Pasword'
        try:
            not_return_password = valid_pasword_field(invalid_password)
        except InvalidString as error:
            self.assertIn(InvalidStringMinSize.message, error.message)
        self.assertEqual(not_return_password, None)

    def test_error_max_size(self):
        """
            Test for raise error: InvalidStringMaxSize
        """
        not_return_password = None
        invalid_password = 'Pasword'*10
        try:
            not_return_password = valid_pasword_field(invalid_password)
        except InvalidString as error:
            self.assertIn(InvalidStringMaxSize.message, error.message)
        self.assertEqual(not_return_password, None)


class ValidSurnameFieldTest(TestCase):
    """
        Check for invalid 'surname'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_surname = valid_surname_field(TEST_USER_SURNAME)
        self.assertEqual(valid_surname, TEST_USER_SURNAME)

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_surname = None
        invalid_surname = b'surnames'
        try:
            not_return_surname = valid_email_field(invalid_surname)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_surname, None)

    def test_error_min_size(self):
        """
            Test for raise error: InvalidStringMinSize
        """
        not_return_surname = None
        invalid_surname = 'Y'
        try:
            not_return_surname = valid_surname_field(invalid_surname)
        except InvalidString as error:
            self.assertIn(InvalidStringMinSize.message, error.message)
        self.assertEqual(not_return_surname, None)

    def test_error_max_size(self):
        """
            Test for raise error: InvalidStringMaxSize
        """
        not_return_surname = None
        invalid_surname = 'Yan'*11
        try:
            not_return_surname = valid_surname_field(invalid_surname)
        except InvalidString as error:
            self.assertIn(InvalidStringMaxSize.message, error.message)
        self.assertEqual(not_return_surname, None)
        #===============================================================================
        #self.assertRaises(InvalidStringMaxSize,error)

    def test_error_characters(self):
        """
            Test for raise error: InvalidCharactersInString
        """
        not_return_surname = None
        invalid_surname = 'User_Test'
        try:
            not_return_surname = valid_surname_field(invalid_surname)
        except InvalidString as error:
            self.assertIn(InvalidCharactersInString.message, error.message)
        self.assertEqual(not_return_surname, None)


class ValidNameFieldTest(TestCase):
    """
        Check for invalid 'name'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_name = valid_name_field(TEST_USER_NAME)
        self.assertEqual(valid_name, TEST_USER_NAME)

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_name = None
        invalid_name = {'name': 'my_name'}
        try:
            not_return_name = valid_email_field(invalid_name)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_name, None)

    def test_error_min_size(self):
        """
            Test for raise error: InvalidStringMinSize
        """
        not_return_name = None
        invalid_name = 'Y'
        try:
            not_return_name = valid_name_field(invalid_name)
        except InvalidString as error:
            self.assertIn(InvalidStringMinSize.message, error.message)
        self.assertEqual(not_return_name, None)

    def test_error_max_size(self):
        """
            Test for raise error: InvalidStringMaxSize
        """
        not_return_name = None
        invalid_name = 'Yan'*11
        try:
            not_return_name = valid_name_field(invalid_name)
        except InvalidString as error:
            self.assertIn(InvalidStringMaxSize.message, error.message)
        self.assertEqual(not_return_name, None)

    def test_error_characters(self):
        """
            Test for raise error: InvalidCharactersInString
        """
        not_return_name = None
        invalid_name = 'User=Test'
        try:
            not_return_name = valid_name_field(invalid_name)
        except InvalidString as error:
            self.assertIn(InvalidCharactersInString.message, error.message)
        self.assertEqual(not_return_name, None)


class ValidPhoneFieldTest(TestCase):
    """
        Check for invalid 'Phone'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_phone = valid_phone_field(TEST_USER_PHONE)
        self.assertEqual(valid_phone, TEST_USER_PHONE)

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_phone = None
        invalid_phone = ['+32456975',2,3]
        try:
            not_return_phone = valid_email_field(invalid_phone)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_phone, None)

    def test_error_min_size(self):
        """
            Test for raise error: InvalidStringMinSize
        """
        not_return_phone = None
        invalid_phone = '+1234567'
        try:
            not_return_phone = valid_phone_field(invalid_phone)
        except InvalidString as error:
            self.assertIn(InvalidStringMinSize.message, error.message)
        self.assertEqual(not_return_phone, None)

    def test_error_max_size(self):
        """
            Test for raise error: InvalidStringMaxSize
        """
        not_return_phone = None
        invalid_phone = '+' + '22'*10
        try:
            not_return_phone = valid_phone_field(invalid_phone)
        except InvalidString as error:
            self.assertIn(InvalidStringMaxSize.message, error.message)
        self.assertEqual(not_return_phone, None)

    def test_error_characters(self):
        """
            Test for raise error: InvalidCharactersInString
        """
        not_return_phone = None
        invalid_phone = '+38(012)123-45-67'
        try:
            not_return_phone = valid_phone_field(invalid_phone)
        except InvalidString as error:
            self.assertIn(InvalidCharactersInString.message, error.message)
        self.assertEqual(not_return_phone, None)


class ValidBirthdayFieldTest(TestCase):
    """
        Checking for invalid 'birthday'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_date = valid_birthday_field(TEST_USER_BIRTHDAY)
        self.assertEqual(valid_date, parser.parse(TEST_USER_BIRTHDAY))

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_date = None
        invalid_date = (1,2)
        try:
            not_return_date = valid_email_field(invalid_date)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_date, None)


    def test_error_invalid_date(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_date = None
        invalid_date = '20122000'
        try:
            not_return_date = valid_birthday_field(invalid_date)
        except InvalidDate as error:
            self.assertEqual(error.message, InvalidDate.message)
        self.assertEqual(not_return_date, None)


class ValidEmailFieldTest(TestCase):
    """
        Check for invalid 'Email. address'
    """

    def test_successful_validation(self):
        """Successful_validation
        """
        valid_phone = valid_email_field(TEST_USER_EMAIL)
        self.assertEqual(valid_phone, TEST_USER_EMAIL)

    def test_type_error(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_date = None
        invalid_date = {}
        try:
            not_return_date = valid_email_field(invalid_date)
        except InvalidType as error:
            self.assertEqual(error.message, InvalidType.message)
        self.assertEqual(not_return_date, None)

    def test_error_invalid_email(self):
        """
            Test for raise error: InvalidDate
        """
        not_return_date = None
        invalid_date = '10.12#%.2000@sads.sa'
        try:
            not_return_date = valid_email_field(invalid_date)
        except InvalidEmail as error:
            self.assertEqual(error.message, InvalidEmail.message)
        self.assertEqual(not_return_date, None)
