"""Test route authorization"""

from tests.test_user import TestUser
from exceptions.validate import InvalidAuthorisation, ErrorAuthorisation
from config.config import (
    TEST_USER_USERNAME,
    TEST_USER_PASSWORD,
    TEST_STATUS_USER,
)


class AuthorizationTest(TestUser):
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
