"""
    Photo_Post module
"""
from sqlalchemy import Integer,Column, ForeignKey
from config.db import db

class PhotoPost(db.Model): # pylint: disable=too-few-public-methods
    """
        Photo_Post model class
    """
    __tablename__ = "Photo_Post"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("Post.id"))
    photo_id = Column(Integer, ForeignKey("User_Photo.id"))

    def __repr__(self):
        return f'User {self.id}'
