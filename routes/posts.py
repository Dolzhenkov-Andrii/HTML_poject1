"""
    User date
"""

# from flask import jsonify
from flask import request
from flask import Blueprint
from databases.models.post import Post
# from databases.models.photo import Photo
from decorators.token import token_required

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/posts', methods=['GET'])
@token_required
def get_posts():
    """
        User Post
    """
    try:
        start = request.args.get('start', default=0, type=int)
        limit = request.args.get('limit', default=10, type=int)
        # postss = Post.query.filter_by(id = 5).all() <- Поиск по Id
        postss = Post.query.order_by(Post.id.desc()).offset(start).limit(limit).all()
        return {'posts': postss, 'code': 200,}
    except TypeError:
        pass
