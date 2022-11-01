"""
    activation_key module
"""

from dataclasses import dataclass
from sqlalchemy import Integer, Column, String, ForeignKey
from databases.models.user import User
from config.db import db


@dataclass
class ActivationKey(db.Model):  # pylint: disable=too-few-public-methods
    """
        activation_key model class
    """
    id: int  # pylint: disable=C0103
    hash_key: str

    __tablename__ = "activation_key"

    id = Column(Integer, primary_key=True)
    hash_key = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return f'ActivationKey {self.id}'
