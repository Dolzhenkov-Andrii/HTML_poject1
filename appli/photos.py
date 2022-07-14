"""
    Posts date
"""

from flask import Blueprint
from databases.models.photo import Photo
photos = Blueprint('photos', __name__, template_folder='templates')


@photos.route('/photos/<name>', methods=['GET'])
def get_photo(name):
    """
        User Post
    """
    user_post = Photo.objects.filters('id', name).get_date[0]
    user_post_dict = user_post.__dict__
    return user_post_dict
