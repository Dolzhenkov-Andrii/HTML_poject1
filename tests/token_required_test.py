"""Test decorator token_required"""
import time
from tests.base_test_class import BaseAPItest
from tokens.token_hendler import TokenManager
from config.config import ACCESS_TOKEN_TIME, SECRET_KEY
from exceptions.token import MissingToken, ExpirationToken, InvalidToken


class TokenRequiredTest(BaseAPItest):
    """refresh_token route tests
        test Valid token
        test Expired token
        test Missing token
        test Invalid token
    """
    URL = '/api/posts_amount'

    def test_valid_token(self):
        """
            Validating a request with
            an active access token
        """
        access_token = {'access_token': TokenManager.create(
            SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': 1})}
        resp = self.client.get(self.URL, headers=access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('size', data)
        self.assertEqual(data['size'], 0)

    def test_expired_token(self):
        """
            Return 401 validation status code and
            message "Request failed due to expiration"
        """
        not_time_life = 0
        expired_token = {'access_token': TokenManager.create(
            SECRET_KEY, not_time_life, {'user_id': 1})}
        time.sleep(1)
        resp = self.client.get(self.URL, headers=expired_token)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.text, ExpirationToken.message)

    def test_missing_token(self):
        """
            Return 401 validation status code and
            message "Request failed due to missing token"
        """
        resp = self.client.get(self.URL)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.text, MissingToken.message)

    def test_invalid_token(self):
        """
            Return 400 validation status code and
            message "Request failed due to token error"
        """
        fake_key = ''
        invalid_token = {'access_token': TokenManager.create(
            fake_key, ACCESS_TOKEN_TIME, {'user_id': 1})}
        resp = self.client.get(self.URL, headers=invalid_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, InvalidToken.message)
