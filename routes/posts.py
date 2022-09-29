"""
    Posts routes
        /posts (args: limit, start)
        /posts/amount
        /post (args: id)
"""

from flask_api import status
from flask import request
from flask import Blueprint
from databases.models.post import Post
from decorators.token import token_required
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/posts', endpoint='get_posts', methods=['GET'])
@token_required
def get_posts():
    """Posts slize
        ?limit=0&start=0
        imit=how many posts (int > 0)
        start=from what position (int > 0)
    """
    start = request.args.get('start', default=0, type=int)
    limit = request.args.get('limit', default=8, type=int)

    if start < 0 or limit < 0:
        start, limit = 0, 8

    slice_posts = Post.query.order_by(
        Post.id.desc()).offset(start).limit(limit).all()
    return {'posts': slice_posts, }, status.HTTP_200_OK


@posts.route('/posts_amount', endpoint='get_amount_posts', methods=['GET'])
@token_required
def get_amount_posts():
    """Size all posts"""
    amount = Post.query.count()
    return {'size': amount, }, status.HTTP_200_OK


@posts.route('/post', endpoint='get_post', methods=['GET'])
@token_required
def get_post():
    """Post
        returns post by id
    """
    post_id = request.args.get('id', default=None, type=int)

    if post_id < 0:
        post_id = None

    post = Post.query.filter_by(id=post_id).first()
    return {'post': post, }, status.HTTP_200_OK
