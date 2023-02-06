'''
    liaison user & post module
'''

from sqlalchemy import Integer, Column, ForeignKey
from config.db import db


class UserPost(db.Model):  # pylint: disable=too-few-public-methods
    '''
        Liaison photo in Post module
    '''
    __tablename__ = 'User_Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

    def __repr__(self):
        return f'Post {self.post_id} = Photo {self.photo_id}'
