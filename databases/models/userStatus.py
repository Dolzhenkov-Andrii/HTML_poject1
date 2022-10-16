"""
    userStatus module
"""
from dataclasses import dataclass
from sqlalchemy import Integer, Column, String
from config.db import db

@dataclass
class UserStatus(db.Model):  # pylint: disable=too-few-public-methods
    """
        userStatus model class
    """
    #id: int # pylint: disable=C0103
    name: str

    __tablename__ = "User_Status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255),nullable=False)

    def __repr__(self):
        return f'UserStatus {self.name}'
