"""Test route authorization"""

from hashlib import pbkdf2_hmac
from tests.base_test_class import BaseAPItest
from databases.models.user import User
from databases.models.userStatus import UserStatus
from exceptions.validate import InvalidAuthorisation, ErrorAuthorisation
from config.config import (
    TEST_USER_USERNAME,
    TEST_USER_PASSWORD,
    TEST_USER_SURNAME,
    TEST_USER_NAME,
    TEST_USER_EMAIL,
    TEST_USER_BIRTHDAY,
    TEST_USER_PHONE,
    TEST_STATUS_USER,
)


class AuthorizationTest(BaseAPItest):
    """
        Authorization class test:
        1) successful authorization, without the mark "remember me"
        2) successful authorization, mark "remember me"
        3) wrong login
        4) wrong password
        5) non-existent user
        6) lack of form
    """
    URL = '/api/authorization'

    def setUp(self):
        super().setUp()
        # Status new user
        user_status = UserStatus()
        user_status.name = TEST_STATUS_USER
        self.test_db.session.add(user_status)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member
        # Test user
        new_user = User()
        pasword = pbkdf2_hmac('sha256',
                              TEST_USER_PASSWORD.encode('utf-8'),
                              b'YtnCjkbD#$%Cfkfnf['*2,
                              100000)
        new_user.pasword = pasword.hex()
        new_user.username = TEST_USER_USERNAME
        new_user.email = TEST_USER_EMAIL
        new_user.surname = TEST_USER_SURNAME
        new_user.name = TEST_USER_NAME
        new_user.birthday = TEST_USER_BIRTHDAY
        new_user.phone = TEST_USER_PHONE
        new_user.status_id = UserStatus.query.filter_by(name=TEST_STATUS_USER).first().id
        self.test_db.session.add(new_user)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member

    def test_authorization(self):
        """
            successful authorization
        """
        auth_form = {
            'username': TEST_USER_USERNAME,
            'password': TEST_USER_PASSWORD,
            'remember_me': False,
        }
        resp = self.client.post(self.URL, json=auth_form)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('access_token', data)
        self.assertIn('refresh_token', data)
        self.assertIn('user', data)
        self.assertEqual(data['user']['status']['name'], TEST_STATUS_USER)
        self.assertEqual(data['user']['username'], auth_form['username'])

    def test_wrong_login(self):
        """
            Test for invalid login,
            401 error and "Wrong login or password" message
        """
        auth_form = {
            'username': 'User1235',
            'password': TEST_USER_PASSWORD,
            'remember_me': False,
        }
        resp = self.client.post(self.URL, json=auth_form)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.text, InvalidAuthorisation.message)

    def test_wrong_password(self):
        """
            Test for invalid password,
            401 error and "Wrong login or password" message
        """
        auth_form = {
            'username': TEST_USER_USERNAME,
            'password': 'password1234',
            'remember_me': False,
        }
        resp = self.client.post(self.URL, json=auth_form)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.text, InvalidAuthorisation.message)

    def test_no_auth_form(self):
        """
           Test for invalid password,
            400 error and "Authorisation Error" message
        """
        auth_form = {}
        resp = self.client.post(self.URL, json=auth_form)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, ErrorAuthorisation.message)
