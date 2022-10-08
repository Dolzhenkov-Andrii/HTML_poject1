"""Test route posts_amount"""
from unittest import TestCase, main
import requests
from tokens.token_hendler import TokenManager
from config.config import ACCESS_TOKEN_TIME
from config.config import SECRET_KEY


class PostsAmountTest(TestCase):
    """posts_amount class test"""
    URL = 'http://127.0.0.1:5050/api/posts_amount'
    access = TokenManager.create(SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': 1, })

    def test_not_404(self):
        """Route exists"""
        resp = requests.get(self.URL)
        self.assertNotEqual(resp.status_code, 404)

    def test_required_token(self):
        """Route is token required"""

        resp = requests.get(self.URL, headers={'access_token': self.access,})
        self.assertEqual(resp.status_code, 200)

    def test_unauthorized_401(self):
        """Not auth (not token)"""
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 401)

    def test_4(self):
        """Invalid token"""
        resp = requests.get(self.URL, headers={'access_token': 'self.access',})
        self.assertEqual(resp.status_code, 500)

    def test_response_size(self):
        """Route response amount posts"""
        resp = requests.get(self.URL, headers={'access_token': self.access,})
        data = resp.json()
        self.assertGreaterEqual(data['size'], 0)


if __name__ == '__main__':
    main()
