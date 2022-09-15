"""
    Configuration
"""

from flask_sqlalchemy import SQLAlchemy
from config.config import DB_HOST, DB_PASSWORD, DB_USER, DB_NAME

# DB_PORT = os.environ.get('DB_PORT', 5050)

DB_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


db = SQLAlchemy()
