"""
    Token Manager
"""
from datetime import datetime, timedelta
import jwt
from flask_api import status
from exceptions.token import DecodeToken


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
                'user': data,
                'expiration': str(datetime.utcnow() + timedelta(seconds=int(time)))
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
        if datetime.fromisoformat(token_data['expiration']) < datetime.utcnow():
            raise DecodeToken
        return True
