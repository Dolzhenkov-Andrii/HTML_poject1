"""
    Configuration
"""
import os

DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = os.environ.get('DB_USER', "root")
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT', 3306)

DB_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
