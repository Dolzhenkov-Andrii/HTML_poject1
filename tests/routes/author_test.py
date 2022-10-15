"""Test route authorization"""
import time
from hashlib import pbkdf2_hmac
from datetime import date
from tests.base_test_class import BaseAPItest
from databases.models.user import User
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
        #Test user
        pasword= pbkdf2_hmac('sha256',
                               'password'.encode('utf-8'),
                               b'YtnCjkbD#$%Cfkfnf['*2,
                               100000)
        new_user = User()
        new_user.username='User'
        new_user.pasword= pasword.hex()
        new_user.email='useremail@gmail.com'
        new_user.surname='Surname'
        new_user.name='Name'
        new_user.birthday= date.today()
        new_user.phone= '+380501234567'
        self.test_db.session.add(new_user) # pylint: disable=no-member
        self.test_db.session.commit() # pylint: disable=no-member


    def test_authorization(self):
        """
            successful authorization, without the mark "remember me"
        """
        auth_form = {
            'username': 'User',
            'password': 'password',
            'remember_me': False,
        }
        resp = self.client.post(self.URL, json=auth_form)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('access_token', data)
        self.assertIn('refresh_token', data)
        self.assertIn('user', data)
        self.assertEqual(data['user']['username'], auth_form['username'])

    def test_auth_remember_me(self):
        """
            successful authorization, mark "remember me"
        """


    def test_wrong_login(self):
        """
            _summary_
        """


    def test_wrong_password(self):
        """
            _summary_
        """


    def test_no_user(self):
        """
            _summary_
        """


    def test_no_auth_form(self):
        """
            _summary_
        """





    # def test_wrong_password(self):
    #     """Wrong password"""
    #     auth_form = {
    #         'username': 'oscurik',
    #         'password': '123456',
    #         'remember_me': True,
    #     }
    #     resp = self.client.post(self.URL, json=auth_form)
    #     self.assertEqual(resp.status_code, 401)

    # def test_no_one_key(self):
    #     """missing one key"""
    #     auth_form = {
    #         'username': 'oscurik',
    #         'remember_me': True,
    #     }
    #     resp = self.client.post(self.URL, data=auth_form)
    #     self.assertEqual(resp.status_code, 400)

    # def test_no_data(self):
    #     """missing the form data"""
    #     resp = self.client.post(self.URL)
    #     self.assertEqual(resp.status_code, 400)
