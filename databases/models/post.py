"""
    Post module
"""

from datetime import datetime
from sqlalchemy import Integer, Column, String, Date, Text, ForeignKey
# from sqlalchemy.orm import relationship
from config.db import db


class Post(db.Model):  # pylint: disable=too-few-public-methods
    """
        Post model class
    """
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    creation_date = Column(Date, default=datetime.utcnow)
    text = Column(Text, nullable=False)
    likes = Column(Integer, nullable=False)
    view = Column(Integer, nullable=False)
    shared = Column(Integer, nullable=False)
    status_id = Column(Integer, ForeignKey('Post_Status.id'),
                       nullable=False)
    # status = relationship('PostStatus')
    category_id = Column(Integer, ForeignKey('Category.id'),
                         nullable=False)
    # category = relationship('Category')

    def __repr__(self):
        return f'Post {self.id}'
