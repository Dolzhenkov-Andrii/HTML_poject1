"""Base class for Test"""
import unittest
import requests
from tokens.token_hendler import TokenManager
from config.config import ACCESS_TOKEN_TIME, REFRESH_REMEMBER_TOKEN_TIME
from config.config import SECRET_KEY


class BaseAPItest(unittest.TestCase):
    """Base class for Test"""
    route_name = ''
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.base_url = f'http://127.0.0.1:5050/api/{self.route_name}'
        self.access_token = TokenManager.create(
            SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': 1, })
        self.refresh_token = TokenManager.create(SECRET_KEY, REFRESH_REMEMBER_TOKEN_TIME, {
            'user_id': 1, 'remember': True})

    def test_not_404(self):
        """Route exists"""
        resp = requests.get(self.base_url)
        self.assertNotEqual(resp.status_code, 404)
