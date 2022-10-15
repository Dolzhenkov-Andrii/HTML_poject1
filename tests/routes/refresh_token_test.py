"""Test route api/refresh_token"""
import time
from tests.base_test_class import BaseAPItest
from tokens.token_hendler import TokenManager
from exceptions.token import MissingToken, ExpirationToken, InvalidToken
from config.config import REFRESH_REMEMBER_TOKEN_TIME
from config.config import SECRET_KEY


class RefreshTokenTest(BaseAPItest):
    """refresh_token route tests
        test Valid token
        test Expired token
        test Missing token
        test Invalid token
    """

    URL = '/api/refresh_token'

    def test_valid_tokens(self):
        """Test for successful receipt of new tokens"""
        refresh_token = {'refresh_token': TokenManager.create(
            SECRET_KEY, REFRESH_REMEMBER_TOKEN_TIME, {'user_id': 1, 'remember': True})}
        resp = self.client.get(self.URL, headers=refresh_token)
        self.assertEqual(resp.status_code, 200)
        tokens = resp.get_json()
        self.assertIn('refresh_token', tokens)
        self.assertIn('access_token', tokens)

    def test_expired_token(self):
        """
            Return 400 validation status code and
            message "Request failed due to expiration"
        """
        not_time_life = 0
        expired_token = {'refresh_token': TokenManager.create(
            SECRET_KEY, not_time_life, {'user_id': 1, 'remember': True})}
        time.sleep(1)
        resp = self.client.get(self.URL, headers=expired_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, ExpirationToken.message)

    def test_missing_token(self):
        """
            Return 400 validation status code and
            message "Request failed due to missing token"
        """
        resp = self.client.get(self.URL)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, MissingToken.message)

    def test_invalid_token(self):
        """
            Return 400 validation status code and
            message "Request failed due to token error"
        """
        fake_key = ''
        invalid_token = {'refresh_token': TokenManager.create(
            fake_key, REFRESH_REMEMBER_TOKEN_TIME, {'user_id': 1, 'remember': True})}
        resp = self.client.get(self.URL, headers=invalid_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, InvalidToken.message)
