"""
    Test route api/account-activation
"""

from tests.test_user import TestUser
from databases.models.activation_key import ActivationKey
from databases.models.user import User
from tokens.token_hendler import TokenManager
from config.config import (
    REFRESH_REMEMBER_TOKEN_TIME,
    SECRET_KEY,
    ACTIVE_USER_STATUS,
    NOT_ACTIVE_USER_STATUS
)

class UserActivationTset(TestUser):
    """Class Test for user activation email"""

    URL = '/api/account-activation'

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

        resp = self.client.get(f'{self.URL}?activation={hash_key}')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('access_token', data)
        self.assertIn('refresh_token', data)
        self.assertIn('user',data)
        self.assertIn('status', data['user'])
        self.assertEqual(data['user']['status']['name'], ACTIVE_USER_STATUS)
