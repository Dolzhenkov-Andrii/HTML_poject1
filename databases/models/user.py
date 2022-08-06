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
