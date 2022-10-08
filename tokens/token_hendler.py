"""
    Token Manager
"""
from datetime import datetime, timedelta
import jwt
from flask_api import status
from validations.json_valid import valid_key
from exceptions.token import DecodeToken
from exceptions.validate import InvalidKey

class TokenManager:
    """TokenManager
    """
    @classmethod
    def create(cls, key, time, data, algoritm='HS256'):
        """Create token

        Args:
            key (str): secret key for token
            time (seconds): token lifetime
            data (dict or str): username or any other information about the user
            algoritm (str): encryption algorithm. Defaults to 'HS256'.

        Returns:
            str: Token
        """
        try:
            token = jwt.encode({
                'data': data,
                'expiration': str(datetime.now() + timedelta(seconds=int(time)))
            }, key, algoritm)
            return token
        except jwt.PyJWTError:
            return DecodeToken.message, status.HTTP_400_BAD_REQUEST

    @classmethod
    def valid(cls, key, token, algoritm='HS256'):
        """Validate token

        Args:
            key (str): secret key for token
            token (str): token
            algoritm (str): encryption algorithm. Defaults to 'HS256'.

        Raises:
            DecodeToken: if key is None or token is None
            DecodeToken: if token life is end

        Returns:
            bool: True - if token life
        """
        if key is None or token is None:
            raise DecodeToken
        token_data = jwt.decode(token, key, algorithms=[algoritm])
        if datetime.fromisoformat(token_data['expiration']) < datetime.now():
            raise DecodeToken
        return True

    @classmethod
    def token_data(cls, key, token, algoritm='HS256'):
        """remembers user

        Args:
            key (str): secret key for token
            token (str): token
            algoritm (str): encryption algorithm. Defaults to 'HS256'.

        Raises:
            DecodeToken: if key is None or token is None
            DecodeToken: if token life is end

        Returns:
            bool: True - if token life
        """
        if key is None or token is None:
            raise DecodeToken
        token_data = jwt.decode(token, key, algorithms=[algoritm])
        try:
            return {'user_id': valid_key(token_data['data'], 'user_id'),
                    'remember': valid_key(token_data['data'], 'remember'),}
        except InvalidKey as error:
            return error.message, status.HTTP_400_BAD_REQUEST
