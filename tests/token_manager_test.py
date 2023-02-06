""" Test token manager
"""
from unittest import TestCase
from tokens.token_hendler import TokenManager
from config.config import (
    SECRET_KEY,
    ACCESS_TOKEN_TIME,
)

class TokenMethodsTest(TestCase):
    """Testing token manager
    """

    token = TokenManager.create(SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': 7, })

    def test_get_id_user(self):
        """ second test
        """
        user_id = TokenManager.get_id_user(SECRET_KEY,self.token)

        self.assertEqual(user_id, 7)
