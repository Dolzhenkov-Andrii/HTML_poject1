"""
    User_Post module
"""
from sqlalchemy import Integer,Column, ForeignKey
from config.db import db

class UserPost(db.Model): # pylint: disable=too-few-public-methods
    """
        User_Post model class
    """
    __tablename__ = "User_Post"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("Post.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)

    def __repr__(self):
        return f'User {self.id}'
