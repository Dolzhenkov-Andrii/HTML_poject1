"""
    Posts date
"""

from flask import Blueprint
from databases.models.post import Post
posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/our_blogs', methods=['GET'])
@posts.route('/our_blogs/<name>', methods=['GET'])
def get_blogs(name=1):
    """
        Posts + Photo
    """
    carent = 1
    start = 0
    posts_dict = {}
    while int(name) > carent:
        start += 6
        carent += 1
    posts_list = [post.photo_posts() for post in Post.objects.offset(f'{start}, 6')]
    posts_dict.update((post.id, post.__dict__) for post in  posts_list)
    return posts_dict


@posts.route('/post/<name>', methods=['GET'])
def get_post(name):
    """
        User Post
    """
    user_post = Post.objects.filters('id',name).get_date[0]
    user_post.photo_posts()
    user_post_dict = user_post.__dict__
    return user_post_dict
