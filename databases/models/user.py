'''
    User module
'''
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Integer, Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from databases.models.userStatus import UserStatus
from databases.models.socialMedia import SocialMedia
from config.db import db


@dataclass
class User(db.Model):  # pylint: disable=too-few-public-methods
    '''
        User model class
    '''
    __tablename__ = 'User'

    id: int  # pylint: disable=C0103
    username: str
    email: str
    surname: str
    name: str
    birthday: datetime
    phone: str
    status: str
    photo: str

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    pasword = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    surname = Column(String(255))
    name = Column(String(255))
    birthday = Column(Date)
    phone = Column(String(255))
    status_id = Column(Integer, ForeignKey(UserStatus.id))
    status = relationship(UserStatus)
    photo = Column(String(255))
    social_media_id = Column(Integer, ForeignKey(
        SocialMedia.id))
    soCmedia = relationship(SocialMedia)


    def __repr__(self):
        return f'User {self.id}'
