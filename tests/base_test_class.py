"""Base class for Test"""
from unittest import TestCase
from app import app, db
from config.config import TEST_DB_URI


class BaseAPItest(TestCase):
    """Parent class for tests"""

    def setUp(self):
        """
            setUp(self) - In each test, creates a test application
            and database based on an existing SQLAlchemy models.
        """
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['TESTING'] = True
        db.init_app(self.app)
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        db.create_all()
        self.test_db = db

    def tearDown(self):
        """
            tearDown(self) - Closes everything and removes
            the database after testing the test
        """
        db.session.remove()
        db.drop_all()
        db.get_engine(self.app).dispose()
        self._ctx.pop()
