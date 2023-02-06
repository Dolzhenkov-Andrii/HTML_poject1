'''
    Photo routes:
        /photo
'''

from flask_api import status
from flask import request
from flask import Blueprint
from databases.models.photo import Photo
from decorators.token import token_required
photos = Blueprint('photos', __name__, template_folder='templates')


@photos.route('/photo', endpoint='get_photo', methods=['GET'])
@token_required
def get_photo():
    '''
        Photo
        ?id=Photo.id
    '''
    photo_id = request.args.get('id', default=None, type=int)

    if photo_id is None or photo_id < 0:
        photo_id = None

    photo = Photo.query.filter_by(id=photo_id).first()
    return {'photo': photo, }, status.HTTP_200_OK
