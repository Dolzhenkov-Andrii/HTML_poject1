"""
    Posts date
"""
from flask import jsonify
from flask import Blueprint
from databases.models.photo import Photo
from decorators.token import token_required
photos = Blueprint('photos', __name__, template_folder='templates')

# test = Photo.query.all()


@photos.route('/photos/<name>', methods=['GET'])
@token_required
def get_photo(name):
    """
        User Post
    """
    test = Photo.query.all()
    return jsonify(test[int(name)-1])
