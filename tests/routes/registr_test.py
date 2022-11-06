"""Test route registration
"""

from tests.test_user import TestUser
from databases.models.user import User
from config.config import (
    NOT_ACTIVE_USER_STATUS,
    TEST_USER_PASSWORD,
    TEST_USER_SURNAME,
    TEST_USER_NAME,
    TEST_USER_BIRTHDAY,
    TEST_USER_PHONE,
)


class RegistrationTest(TestUser):
    """
        Registrations class test:
        1) Successful registration
        2)
    """
    URL = '/api/new-user'

    def test_successful_registration(self):
        """Successful registration"""
        registr_form = {
                'username': 'oscur1k2',
                'password': TEST_USER_PASSWORD,
                'email': 'oscurabow@gmail.com',
                'surname': TEST_USER_SURNAME+'-new',
                'name': TEST_USER_NAME+'-new',
                'birthday': TEST_USER_BIRTHDAY,
                'phone': TEST_USER_PHONE+'5',
            }
        resp = self.client.post(self.URL, json=registr_form)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            registr_form['email'],
            User.query.filter_by(username=registr_form['username']).first().email
            )
        self.assertEqual(
            NOT_ACTIVE_USER_STATUS,
            User.query.filter_by(username=registr_form['username']).first().status.name
        )
