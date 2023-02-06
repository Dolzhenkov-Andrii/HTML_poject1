'''
    socialMedia module
'''

from sqlalchemy import Integer, Column, String
from config.db import db

class SocialMedia(db.Model):  # pylint: disable=too-few-public-methods
    '''
        socialMedia model class
    '''
    __tablename__ = 'Social_media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Telegram = Column(String(255),nullable=False)
    Instagram = Column(String(255),nullable=False)
    Twitter = Column(String(255),nullable=False)
    YouTube = Column(String(255),nullable=False)
    Facebook = Column(String(255),nullable=False)

    def __repr__(self):
        return f'SocialMedia {self.id}'
