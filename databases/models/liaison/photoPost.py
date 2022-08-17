"""
    liaison photo & post module
"""

from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from config.db import db


class PhotoPost(db.Model):  # pylint: disable=too-few-public-methods
    """
        Liaison photo in Post module
    """
    __tablename__ = "User_Photo"
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, ForeignKey("User_Photo.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("Post.id"), nullable=False)
    posts = relationship('Post', back_populates='photos', cascade='all')

    def __repr__(self):
        return f'Post {self.post_id} = Photo {self.photo_id}'
