"""
    Posts date
"""

from flask import Blueprint
from databases.models.photo import Photo
photos = Blueprint('photos', __name__, template_folder='templates')


@photos.route('/photo/<name>')
def post(name):
    """
        User Post
    """
    user_post = Photo.objects.filters('id', name).get_date[0]
    user_post_dict = user_post.__dict__
    return user_post_dict
