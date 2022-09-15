"""
    User date
"""

# from flask import jsonify
from flask import Blueprint
from databases.models.post import Post
from decorators import token_required
# from databases.models.photo import Photo
# from databases.models.photoPost import PhotoPost
# from databases.models.postStatus import PostStatus

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/posts/<name>', methods=['GET'])
@token_required
def get_photo(name):
    """
        User Post
    """
    try:
        postss = Post.query.all()

        return {'posts': postss, 'code': 200, 'name':name}
    except TypeError:
        pass
