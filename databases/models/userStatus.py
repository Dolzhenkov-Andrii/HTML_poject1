"""
    userStatus module
"""

from sqlalchemy import Integer, Column, String
from config.db import db

class UserStatus(db.Model):  # pylint: disable=too-few-public-methods
    """
        userStatus model class
    """
    __tablename__ = "User_Status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255),nullable=False)

    def __repr__(self):
        return f'UserStatus {self.name}'
