# '''
#     Photo_Post association table
# '''

# from sqlalchemy import Integer,Column, ForeignKey, Table
# from config.db import db

# link_photo_post = Table('Photo_Post', db.metadata,
#                          Column('post_id', Integer, ForeignKey('Post.id'), nullable=False),
#                          Column('photo_id', Integer, ForeignKey('User_Photo.id'), nullable=False))

