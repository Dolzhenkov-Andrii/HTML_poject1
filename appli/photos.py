"""
    Posts date
"""


from flask import Blueprint
from databases.models.photo import Photo

photos = Blueprint('photos', __name__, template_folder='templates')

# test = Photo.query.all()


@photos.route('/photos/<name>', methods=['GET'])
def get_photo(name):
    """
        User Post
    """
    test = Photo.query.all()
    return {f'test{name}': f'{test[int(name)-1].photo}'}
