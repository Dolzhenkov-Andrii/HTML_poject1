"""
    New test user
"""

from hashlib import pbkdf2_hmac
from dateutil import parser
from tests.base_test_class import BaseAPItest
from tokens.token_hendler import TokenManager
from databases.models.user import User
from databases.models.userStatus import UserStatus
from config.config import (
    ACCESS_TOKEN_TIME,
    SECRET_KEY,
    TEST_USER_USERNAME,
    TEST_USER_PASSWORD,
    TEST_USER_SURNAME,
    TEST_USER_NAME,
    TEST_USER_EMAIL,
    TEST_USER_BIRTHDAY,
    TEST_USER_PHONE,
    PASSWORD_SALT,
    NOT_ACTIVE_USER_STATUS,
)


class TestUser(BaseAPItest):
    """
        Creates a test user in the database
         to be able to test queries
    """

    def setUp(self):
        super().setUp()
        # Status new user
        user_status = UserStatus()
        user_status.name = NOT_ACTIVE_USER_STATUS
        self.test_db.session.add(user_status)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member
        # Test user
        new_user = User()
        pasword = pbkdf2_hmac('sha256',
                              TEST_USER_PASSWORD.encode('utf-8'),
                              PASSWORD_SALT.encode('utf-8'),
                              100000)
        new_user.pasword = pasword.hex()
        new_user.username = TEST_USER_USERNAME
        new_user.email = TEST_USER_EMAIL
        new_user.surname = TEST_USER_SURNAME
        new_user.name = TEST_USER_NAME
        new_user.birthday = parser.parse(TEST_USER_BIRTHDAY)
        new_user.phone = TEST_USER_PHONE
        new_user.status_id = UserStatus.query.filter_by(
            name=NOT_ACTIVE_USER_STATUS).first().id
        self.test_db.session.add(new_user)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member
        self.access_token = {'access_token': TokenManager.create(
            SECRET_KEY, ACCESS_TOKEN_TIME, {'user_id': 1, }), }
        self.user_id = User.query.filter_by(
            username=TEST_USER_USERNAME).first().id
