"""
    User rout
"""


from flask import Blueprint
from databases.models.user import User

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/user/<name>', methods=['GET'])
def get_photo(name):
    """
        User
    """
    test = User.query.all()

    return {f'test{name}': f'{test[int(name)-1].username}'}
