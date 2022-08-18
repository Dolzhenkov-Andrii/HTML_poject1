"""
    Posts date
"""




from flask import Blueprint
from databases.models.photo import Photo

photos = Blueprint('photos', __name__, template_folder='templates')

# test = Photo.query.all()

@photos.route('/photos/<name>', methods=['GET'])
def get_photo(name):
    """
        User Post
    """

    print('='*20)
    print('@photos.route = ', Photo)
    print('='*20)
    test = Photo.query.all()
    # test = Photo
    print(f'{test}')
    return {f'test {name}' : f'{test[int(name)-1].photo}'}
