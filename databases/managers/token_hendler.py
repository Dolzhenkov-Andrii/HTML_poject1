"""
    Token Manager
"""
from datetime import datetime, timedelta
import jwt
from exceptionsAPI.exceptionsAPI import DecodeToken

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
            return DecodeToken.message, DecodeToken.code

    @classmethod
    def valid(cls, key, token, algoritm='HS256'):
        """Valid token

        Args:
            key (str): secret key for token decode
            token (str): token
            algoritm (str): encryption algorithm. Defaults to 'HS256'.

        Returns:
            bool: Token expiration date (True or False)
        """
        try:
            if key is None or token is None:
                return False

            token_data = jwt.decode(token, key, algorithms=[algoritm])
            if datetime.fromisoformat(token_data['expiration']) < datetime.utcnow():
                return False
            return True
        except jwt.PyJWTError:
            return DecodeToken.message, DecodeToken.code
