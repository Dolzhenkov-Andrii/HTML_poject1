"""
    Config
"""
import os
APP_HOST = '127.0.0.1'
APP_PORT = 5050
APP_TEST_URL = f'{APP_HOST}:{APP_PORT}'

DB_HOST = os.environ.get('DB_HOST',"127.0.0.1")
DB_PASSWORD = os.environ.get('DB_PASSWORD',"Ujhs!!Gj04Rjktyj!((#")
DB_USER = os.environ.get('DB_USER',"oscura")
DB_NAME = os.environ.get('DB_NAME','my_blog')
SECRET_KEY = os.environ.get('SECRET_KEY',"cfb1ebd916608f13e6d08cad30521dcc")
# ACCESS_TOKEN_TIME = os.environ.get('ACCESS_TOKEN_TIME')
# REFRESH_TOKEN_TIME = os.environ.get('REFRESH_TOKEN_TIME')
# REFRESH_REMEMBER_TOKEN_TIME = os.environ.get('REFRESH_REMEMBER_TOKEN_TIME')
ACCESS_TOKEN_TIME = '15'
REFRESH_TOKEN_TIME = '25'
REFRESH_REMEMBER_TOKEN_TIME = '35'


