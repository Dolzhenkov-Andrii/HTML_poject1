'''
    Posts routes
        /posts (args: position, amount)
        /post (args: id)
'''

from flask_api import status
from flask import request
from flask import Blueprint
from service.upload_image import UploadImage
from databases.models.post import Post, PostStatus
from databases.models.photo import Photo
from decorators.token import token_required
from exceptions.posts import PostArgsError, APIexception
from exceptions.token import DecodeToken
from exceptions.validate import InvalidImage
from config.db import db
from config.config import BASE_COUNT_POSTS, BASE_POSITION_POSTS, SECRET_KEY, ACTIVE_POST_STATUS
from validations.routes.new_post import PostValid
from tokens.token_hendler import TokenManager


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/posts', endpoint='get_posts', methods=['GET'])
@token_required
def get_posts():
    '''Posts slize
        ?position=0&amount=0
    '''

    position = request.args.get('position', default=BASE_POSITION_POSTS, type=int)
    amount = request.args.get('amount', default=BASE_COUNT_POSTS, type=int)

    if position < 0 or amount < 0:
        return PostArgsError.message, status.HTTP_400_BAD_REQUEST

    slice_posts = Post.query.order_by(
        Post.id.desc()).offset(position).limit(amount).all()
    amount = Post.query.count()

    return {'posts': slice_posts, 'size': amount}, status.HTTP_200_OK



@posts.route('/new-post', endpoint='set_post', methods=['POST'])
@token_required
def set_post():
    '''Post
        add new post

        title: str
        text: str
        status: str
        likes: int
        view: int
        shared: int
        user: User
        photos: Photo
    '''

    try:
        post_form = PostValid(**request.form)
        validate_date = post_form.validate()
    except APIexception as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    try:
        user_id = TokenManager.get_id_user(SECRET_KEY ,request.headers['Access-Token'])
    except DecodeToken as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    img_photo = None
    if request.method == 'POST' and 'file' in request.files:
        try:
            img_photo = UploadImage(request.files['file']).save_image()
        except InvalidImage as error:
            return error.message, status.HTTP_400_BAD_REQUEST

    post_status = PostStatus.query.filter_by(name=ACTIVE_POST_STATUS).first()
    if post_status is None:
        status_post = PostStatus()
        status_post.name = ACTIVE_POST_STATUS
        db.session.add(status_post)  # pylint: disable=no-member
        db.session.commit()  # pylint: disable=no-member

    try:
        new_post = Post()
        new_post.title = validate_date['title']
        new_post.text = validate_date['text']
        new_post.status_id = PostStatus.query.filter_by(name=ACTIVE_POST_STATUS).first().id
        new_post.user_id = user_id
        db.session.add(new_post)  # pylint: disable=no-member
        db.session.commit()  # pylint: disable=no-member
        if img_photo is not None:
            photo = Photo()
            photo.photo = img_photo
            photo.user_id = user_id
            photo.post_id = new_post.id
            db.session.add(photo)  # pylint: disable=no-member
            db.session.commit()  # pylint: disable=no-member

    except APIexception as error:
        return error.message, status.HTTP_400_BAD_REQUEST

    return {'post' : new_post}, status.HTTP_200_OK
