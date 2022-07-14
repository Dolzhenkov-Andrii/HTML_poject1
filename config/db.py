"""
    Configuration
"""
import os

DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = os.environ.get('DB_USER', "root")
DB_NAME = os.environ.get('DB_NAME')
