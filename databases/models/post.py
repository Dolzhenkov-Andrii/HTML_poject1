'''
    Post module
'''

from dataclasses import dataclass
from datetime import date, datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Date, Text, ForeignKey
from databases.models.user import User
from databases.models.photo import Photo
from databases.models.category import Category
from databases.models.postStatus import PostStatus
from config.db import db

@dataclass
class Post(db.Model):  # pylint: disable=too-few-public-methods
    '''
        Post model class
    '''
    id: int # pylint: disable=C0103
    title: str
    creation_date: date
    text: str
    status: str
    user: User
    photos: Photo

    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    creation_date = Column(Date, nullable=False, default=datetime.utcnow)
    text = Column(Text, nullable=False)
    status_id = Column(Integer, ForeignKey(PostStatus.id))
    status = relationship(PostStatus)
    category_id = Column(Integer, ForeignKey(Category.id))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship(User, backref='posts', lazy=True)
    photos = relationship(Photo,backref='Post')

    def __repr__(self):
        return f'Post {self.id}'
