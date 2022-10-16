"""Config

    APP_HOST
    APP_PORT
    DB_HOST
    DB_PASSWORD
    DB_USER
    DB_NAME
    SECRET_KEY
    ACCESS_TOKEN_TIME
    REFRESH_TOKEN_TIME
    REFRESH_REMEMBER_TOKEN_TIME


    TEST_DB_PASSWORD
    TEST_DB_USER
    TEST_DB_NAME
    TEST_DB_URI
    TEST_USER_ID
    TEST_USER_PASSWORD
    TEST_USER_USERNAME
    TEST_USER_EMAIL
    TEST_USER_SURNAME
    TEST_USER_NAME
    TEST_USER_BIRTHDAY
    TEST_USER_PHONE
    TEST_STATUS_USER
    TEST_PHOTO_PHOTO
"""
import os
from datetime import date


APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
APP_PORT = os.environ.get('APP_PORT', 5050)

DB_HOST = os.environ.get('DB_HOST', "127.0.0.1")
DB_PASSWORD = os.environ.get('DB_PASSWORD', "Ujhs!!Gj04Rjktyj!((#")
DB_USER = os.environ.get('DB_USER', "oscura")
DB_NAME = os.environ.get('DB_NAME', 'my_blog')

SECRET_KEY = os.environ.get('SECRET_KEY', "cfb1ebd916608f13e6d08cad30521dcc")
# ACCESS_TOKEN_TIME = os.environ.get('ACCESS_TOKEN_TIME')
# REFRESH_TOKEN_TIME = os.environ.get('REFRESH_TOKEN_TIME')
# REFRESH_REMEMBER_TOKEN_TIME = os.environ.get('REFRESH_REMEMBER_TOKEN_TIME')
ACCESS_TOKEN_TIME = '15'
REFRESH_TOKEN_TIME = '25'
REFRESH_REMEMBER_TOKEN_TIME = '35'


TEST_DB_PASSWORD = os.environ.get(
    'DB_TEST_PASSWORD', 'Yt123Ghblevfk$%^Gfhjkm789')
TEST_DB_USER = os.environ.get('DB_TEST_USER', 'test')
TEST_DB_NAME = os.environ.get('DB_TEST_NAME', 'test_my_blog')
TEST_DB_URI = os.environ.get('TEST_DB_URI',
                             f'mysql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{DB_HOST}/{TEST_DB_NAME}')

TEST_USER_ID = os.environ.get('TEST_USER_ID', 1)
TEST_USER_PASSWORD = os.environ.get('TEST_USER_PASSWORD', 'password')
TEST_USER_USERNAME = os.environ.get('TEST_USER_USERNAME', 'User')
TEST_USER_EMAIL = os.environ.get('TEST_USER_EMAIL', 'useremail@gmail.com')
TEST_USER_SURNAME = os.environ.get('TEST_USER_SURNAME', 'Surname')
TEST_USER_NAME = os.environ.get('TEST_USER_NAME', 'Name')
TEST_USER_BIRTHDAY = os.environ.get('TEST_USER_PHONE', date.today())
TEST_USER_PHONE = os.environ.get('TEST_USER_PHONE', '+380501234567')
TEST_STATUS_USER = os.environ.get('TEST_STATUS_USER', 'user')
TEST_STATUS_POST = os.environ.get('TEST_STATUS_USER', 'Active')
TEST_PHOTO_PHOTO = os.environ.get('TEST_PHOTO_PHOTO', 'url/photo')
TEST_POST_TITLE = os.environ.get('TEST_PHOTO_PHOTO', 'Test Posts')
TEST_POST_TEXT = os.environ.get(
    'TEST_POST_TEXT', "We check what works, otherwise what's the point of writing them.")
