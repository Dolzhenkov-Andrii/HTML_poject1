"""Test route authorization"""
from unittest import main
import requests
from tests.base_test_class import BaseAPItest

class AuthorizationTest(BaseAPItest):
    """authorization class test"""
    route_name = 'authorization'

    def test_successful_auth(self):
        """Successful authorization"""
        auth_form = {
            'username': 'oscurik',
            'password': 'pass123',
            'remember_me': True,
        }
        resp = requests.post(self.base_url,json=auth_form)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn('access_token', data)
        self.assertIn('refresh_token', data)
        self.assertIn('user', data)
        self.assertEqual(data['user']['username'], auth_form['username'])

    def test_wrong_password(self):
        """Wrong password"""
        auth_form = {
            'username': 'oscurik',
            'password': '123456',
            'remember_me': True,
        }
        resp = requests.post(self.base_url,json=auth_form)
        self.assertEqual(resp.status_code, 401)

    def test_no_one_key(self):
        """missing one key"""
        auth_form = {
            'username': 'oscurik',
            'remember_me': True,
        }
        resp = requests.post(self.base_url,json=auth_form)
        self.assertEqual(resp.status_code, 400)

    def test_no_data(self):
        """missing the form data"""
        resp = requests.post(self.base_url)
        self.assertEqual(resp.status_code, 400)



if __name__ == '__main__':
    main()
