"""
    Configuration
"""

from flask_sqlalchemy import SQLAlchemy
from config.config import DB_HOST, DB_PASSWORD, DB_USER, DB_NAME
from config.config import DB_TEST_NAME, DB_TEST_USER, DB_TEST_PASSWORD

DB_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
DB_TEST_URI = f'mysql://{DB_TEST_USER}:{DB_TEST_PASSWORD}@{DB_HOST}/{DB_TEST_NAME}'

db = SQLAlchemy()
