"""
    tmp
"""

from flask import jsonify
from flask import Blueprint
from databases.models.userStatus import UserStatus
from decorators.token import token_required
status = Blueprint('status', __name__, template_folder='templates')


@status.route('/status/<name>', methods=['GET'])
@token_required
def get_status(name):
    """
        User Post
    """
    tmp = name
    test = UserStatus.query.all()
    if not test:
        tmp = 1
        test = [{'id': 0, 'name': 'Error'}]
    return jsonify(test[int(tmp)-1])
