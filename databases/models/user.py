"""
    User module
"""
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

# from databases.models.photo import Photo

from config.db import db

class User(db.Model): # pylint: disable=too-few-public-methods
    """
        User model class
    """
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    photos = relationship(
        'databases.models.photo.Photo', back_populates='users'
    )
    # photo = Column(String(255))
    # user = relationship(
    #     'User', back_populates='photos', cascade='all, delete-orphan'
    # )

    # table_name = 'User_Photo'
    # manager_class = BaseManager


#-------------------------------------------------------------
#-------------------------------------------------------------
# from sqlalchemy import Integer, Column, String, Date, ForeignKey
# from sqlalchemy.orm import relationship
# from config.db import db


# class User(db.Model):  # pylint: disable=too-few-public-methods
#     """
#         User model class
#     """
#     __tablename__ = "User"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(255), nullable=False, unique=True)
#     password = Column(String(255), nullable=False)
#     email = Column(String(255), nullable=False, unique=True)
#     surname = Column(String(255), nullable=False)
#     name = Column(String(255), nullable=False)
#     birthday = Column(Date, nullable=False)
#     phone = Column(String(255), nullable=False)
#     status_id = Column(Integer, ForeignKey('User_Status.id'))
#     status = relationship('UserStatus')
#     social_media_id = Column(Integer, ForeignKey('Social_media.id'))
#     soCmedia = relationship('SocialMedia')

#     def __repr__(self):
#         return f'User {self.id}'
