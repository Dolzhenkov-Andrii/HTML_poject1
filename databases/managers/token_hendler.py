"""
    Token Manager
"""

from datetime import datetime, timedelta
import jwt


def create_token(key, time, data, algoritm='HS256'):
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

        # return token
    except jwt.InvalidTokenError as error:
        return {'code': 17000, 'message': error}
    return token


def valid_token(key, token, algoritm='HS256'):
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
            # return {'Error': 'Invalid args', 'message': 'Not have token or key'}
            return False

        token_data = jwt.decode(token, key, algorithms=[algoritm])
        if datetime.fromisoformat(token_data['expiration']) < datetime.utcnow():
            return False
        # return True
    except jwt.ExpiredSignatureError as error:
        return {'code': 17001, 'message': error}
    return True


class TokenManager:
    """TokenManager
    """

    def create(self, key, time, data, algoritm='HS256'):
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
        except jwt.InvalidTokenError as error:
            return {'error_code': error, 'message': 'Error creating token'}

    def valid(self, key, token, algoritm='HS256'):
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
                # return {'Error': 'Invalid args', 'message': 'Not have token or key'}
                return False

            token_data = jwt.decode(token, key, algorithms=[algoritm])
            if datetime.fromisoformat(token_data['expiration']) < datetime.utcnow():
                return False
            return True
        except jwt.ExpiredSignatureError as error:
            return {'error_code': error, 'message': 'Signature has expired'}
