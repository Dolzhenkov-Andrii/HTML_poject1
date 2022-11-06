"""
    Test route api/account-reactivation
"""

from tests.test_user import TestUser
from databases.models.activation_key import ActivationKey
from databases.models.user import User
from tokens.token_hendler import TokenManager
from config.config import (
    REFRESH_REMEMBER_TOKEN_TIME,
    SECRET_KEY,
    NOT_ACTIVE_USER_STATUS,
    TEST_USER_USERNAME,
    TEST_USER_PASSWORD,
)

class UserReactivationTset(TestUser):
    """Class Test for user reactivation email"""

    URL = '/api/account-reactivation'

    def test_valid_activation_key(self):
        """Successful activation and status change to active"""
        hash_key = TokenManager.create(
        SECRET_KEY, REFRESH_REMEMBER_TOKEN_TIME, {'user_id': 1, })
        activ_key = ActivationKey()
        activ_key.hash_key = hash_key
        activ_key.user_id = 1
        self.test_db.session.add(activ_key)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member

        self.assertEqual(
            User.query.filter_by(id=1).first().status.name,
            NOT_ACTIVE_USER_STATUS
        )

        auth_form = {
            'username': TEST_USER_USERNAME,
            'password': TEST_USER_PASSWORD,
            'remember_me': False,
        }
        resp = self.client.post(self.URL, json=auth_form)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('username', data)
        self.assertIn('email', data)
