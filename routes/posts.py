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
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/posts', endpoint='get_posts', methods=['GET'])
@token_required
def get_posts():
    """Posts slize
        ?amount=0&amount=0
        amount=how many posts (int > 0)
        position=from what position (int > 0)
    """
    my_cooki = request.cookies.get('access_token', None)
    my_user = request.cookies.get('Name', None)

    position = request.args.get('position', default=0, type=int)
    amount = request.args.get('amount', default=6, type=int)

    if position < 0 or amount < 0:
        position, amount = 0, 8

    slice_posts = Post.query.order_by(
        Post.id.desc()).offset(position).limit(amount).all()
    return {'posts': slice_posts,
            'my_cooki':{'my_access':my_cooki, 'my_user':my_user,}},status.HTTP_200_OK


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
