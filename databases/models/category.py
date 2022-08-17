"""
    Category module
"""

from sqlalchemy import Integer, Column, String
from config.db import db

class Category(db.Model):  # pylint: disable=too-few-public-methods
    """
        Category model class
    """
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False)

    def __repr__(self):
        return f'Category {self.name}'
