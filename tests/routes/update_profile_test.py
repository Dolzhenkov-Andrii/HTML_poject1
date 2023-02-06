"""
    Test for update profile user
"""

# from dateutil import parser
from tests.test_user import TestUser
from config.config import (
    TEST_USER_NAME,
    TEST_USER_PHONE,
    TEST_USER_SURNAME,
    # TEST_USER_BIRTHDAY,
)

class TestUpdateProfie(TestUser):
    """
        Test updte profile user in database
    """

    URL = '/api/user/update'

    def setUp(self):
        super().setUp()
        self.test_form = {
            'surname': 'TestSurname',
            'name': 'TestName',
            'phone': '+380991234567',
            'birthday': '1999-12-12',
        }

    def test_successful_update(self):
        """ Profile update request
        """

        self.assertEqual(self.test_user.surname, TEST_USER_SURNAME)
        self.assertEqual(self.test_user.name, TEST_USER_NAME)
        self.assertEqual(self.test_user.phone, TEST_USER_PHONE)
        # self.assertEqual(self.test_user.birthday, parser.parse(TEST_USER_BIRTHDAY))
        resp = self.client.post(self.URL, json=self.test_form, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_user.surname, self.test_form['surname'])
        self.assertEqual(self.test_user.name, self.test_form['name'])
        self.assertEqual(self.test_user.phone, self.test_form['phone'])
        # self.assertEqual(self.test_user.birthday, self.test_form)
