"""
    Posts routes
        /posts (args: position, amount)
        /posts/amount
        /post (args: id)
"""

from flask_api import status
from flask import request
from flask import Blueprint
from databases.models.post import Post
from decorators.token import token_required
from exceptions.posts import PostArgsError
from config.config import BASE_COUNT_POSTS, BASE_POSITION_POSTS

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/posts', endpoint='get_posts', methods=['GET'])
@token_required
def get_posts():
    """Posts slize
        ?position=0&amount=0
    """

    position = request.args.get('position', default=BASE_POSITION_POSTS, type=int)
    amount = request.args.get('amount', default=BASE_COUNT_POSTS, type=int)

    if position < 0 or amount < 0:
        return PostArgsError.message, status.HTTP_400_BAD_REQUEST

    slice_posts = Post.query.order_by(
        Post.id.desc()).offset(position).limit(amount).all()
    return {'posts': slice_posts}, status.HTTP_200_OK


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

    if post_id is None or post_id < 0:
        return PostArgsError.message, status.HTTP_400_BAD_REQUEST

    post = Post.query.filter_by(id=post_id).first()
    return {'post': post, }, status.HTTP_200_OK
