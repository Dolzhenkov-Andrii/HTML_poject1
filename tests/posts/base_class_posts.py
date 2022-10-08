"""Base class for Posts Test"""
import requests
from tests.base_test_class import BaseAPItest


class BasePostsTest(BaseAPItest):
    """Base class for Test"""

    def test_unauthorized_401(self):
        """Not auth (not token)"""
        resp = requests.get(self.base_url)
        self.assertEqual(resp.status_code, 401)

    def test_invalid_token(self):
        """Invalid token"""
        resp = requests.get(self.base_url, headers={
                            'access_token': 'self.access', })
        self.assertEqual(resp.status_code, 500)
