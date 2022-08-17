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
    print('FALSE Photo = ', Photo)
    print('='*20)
    test = Photo.qeury.all()
    # test = Photo
    print(f'{name} = ',test)
    return test
