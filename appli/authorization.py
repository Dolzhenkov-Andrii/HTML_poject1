"""
    Authorization date
"""


from flask import Blueprint, request

author = Blueprint('author', __name__, template_folder='templates')


@author.route('/authorization', methods=['POST'])
def autho_form():
    """
        Authorization form
    """
    # print(uuid)
    authoForm = request.get_json()
    tmp2 = {0: f'{authoForm}', 1: 'test', }
    if (authoForm['login'] == 'test'):
        tmp2 = {1: 'YES', }
    else:
        tmp2 = {1: 'NO', }
    return str(tmp2)
