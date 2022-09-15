"""
    Post module
"""
from dataclasses import dataclass
from datetime import date, datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Date, Text, ForeignKey
from databases.models.user import User
from config.db import db

@dataclass
class Post(db.Model):  # pylint: disable=too-few-public-methods
    """
        Post model class
    """
    id: int # pylint: disable=C0103
    title: str
    creation_date: date
    text: str
    likes: int
    view: int
    shared: int
    user: User

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
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User, backref='posts', lazy=True)

    def __repr__(self):
        return f'Post {self.id}'
