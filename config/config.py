"""
    Config
"""
import os

DB_HOST = os.environ.get('DB_HOST')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
SECRET_KEY = os.environ.get('SECRET_KEY')
ACCESS_TOKEN_TIME = os.environ.get('ACCESS_TOKEN_TIME')
REFRESH_TOKEN_TIME = os.environ.get('REFRESH_TOKEN_TIME')
REFRESH_REMEMBER_TOKEN_TIME = os.environ.get('REFRESH_REMEMBER_TOKEN_TIME')
