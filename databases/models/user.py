"""
    User module
"""
from sqlalchemy import Integer, Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from databases.models.userStatus import UserStatus
from databases.models.socialMedia import SocialMedia

from config.db import db


class User(db.Model):  # pylint: disable=too-few-public-methods
    """
        User model class
    """
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    pasword = Column(String(255))
    email = Column(String(255), unique=True)
    surname = Column(String(255))
    name = Column(String(255))
    birthday = Column(Date)
    phone = Column(String(255))
    status_id = Column(Integer, ForeignKey('User_Status.id'), nullable=False)
    status = relationship(UserStatus)
    social_media_id = Column(Integer, ForeignKey(
        'Social_media.id'), nullable=False)
    soCmedia = relationship(SocialMedia)

    def __repr__(self):
        return f'User {self.id}'
