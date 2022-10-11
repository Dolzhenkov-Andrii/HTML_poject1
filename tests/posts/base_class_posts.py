"""Base class for Posts Test"""
from tests.base_test_class import BaseAPItest
from tokens.token_hendler import TokenManager
from config.config import ACCESS_TOKEN_TIME
from config.config import SECRET_KEY

class BasePostsTest(BaseAPItest):
    """Base class for Test"""

    def setUp(self):
        super().setUp()
        self.access_token = {'access_token': TokenManager.create(
            SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': 1, }), }
