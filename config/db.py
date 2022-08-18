"""
    Configuration
"""

import os
from flask_sqlalchemy import SQLAlchemy


DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'Ujhs!!Gj04Rjktyj!((#')
DB_USER = os.environ.get('DB_USER', "oscura")
DB_NAME = os.environ.get('DB_NAME', "my_blog")
# DB_PORT = os.environ.get('DB_PORT', 5050)

DB_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


db = SQLAlchemy()
