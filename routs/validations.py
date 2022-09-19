"""Routs validations
"""
# from flask_api import status
from hashlib import pbkdf2_hmac
from databases.models.user import User
from databases.managers.json_valid import request_data
from exceptionsAPI import exceptionsAPI


class Authorization:
    """Authorization check
    """
    username = None
    password = None
    json_data = None
    user = None

    def __init__(self, json_data):
        self.json_data = json_data

    def valid_json_key(self):
        """Key verification
        """
        try:
            if self.json_data:
                self.username = request_data(self.json_data, 'login')
                self.password = request_data(self.json_data, 'password')
            raise exceptionsAPI.InvalidLoginOrPassword
        except exceptionsAPI.InvalidLoginOrPassword as error:
            return error.message, error.code

    def valid(self):
        """Validation Authorization
        """
        try:
            self.valid_json_key()
            self.user = User.query.filter_by(username=f'{self.username}').first()
            hash_key = pbkdf2_hmac('sha256',
                                 self.password.encode('utf-8'),
                                 b'YtnCjkbD#$%Cfkfnf['*2,
                                 100000)

            if self.user and self.user.pasword == hash_key.hex():
                return True
            raise exceptionsAPI.InvalidLoginOrPassword

        except exceptionsAPI.InvalidLoginOrPassword as error:
            return error.message, error.code
