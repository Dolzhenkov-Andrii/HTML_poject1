"""
    postStatus module
"""

from sqlalchemy import Integer, Column, String
from config.db import db

class PostStatus(db.Model):  # pylint: disable=too-few-public-methods
    """
        postStatus model class
    """
    __tablename__ = "Post_Status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255),nullable=False)

    def __repr__(self):
        return f'PostStatus {self.name}'
