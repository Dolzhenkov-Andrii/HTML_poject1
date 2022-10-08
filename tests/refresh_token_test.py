"""Test route refresh_token"""
from unittest import main
import requests
from tests.base_test_class import BaseAPItest


class RefreshTokenTest(BaseAPItest):
    """refresh_token class test"""
    route_name = 'refresh_token'

    def test_receiving_tokens(self):
        """Return of tokens"""
        resp = requests.get(self.base_url, headers={'refresh_token': self.refresh_token,})
        tokens = resp.json()
        self.assertEqual(resp.status_code, 200)
        self.assertIn('refresh_token', tokens)
        self.assertIn('access_token', tokens)

    def test_no_token(self):
        """missing access token"""
        resp = requests.get(self.base_url)
        self.assertEqual(resp.status_code, 400)

    def test_invalid_token(self):
        """Invalid token"""
        resp = requests.get(self.base_url, headers={
                            'refresh_token': 'self.refresh_token', })
        self.assertEqual(resp.status_code, 500)

if __name__ == '__main__':
    main()
