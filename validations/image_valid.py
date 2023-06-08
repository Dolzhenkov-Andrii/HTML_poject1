""" Validator Image
"""

from werkzeug.utils import secure_filename

from config.config import ALLOWED_EXTENSIONS
from exceptions.validate import InvalidImage, InvalidImageFormat

def allowed_file(filename):
    """ Validate img extensions
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class ImageValidName:
    """ Validate name img and extensions
    """

    def __init__(self, image):
        self.image = image

    def validate(self):
        """ valid name file and extensions
        """
        if self.image is None or self.image.filename == '':
            raise InvalidImage

        if allowed_file(self.image.filename) is False:
            raise InvalidImageFormat

        img_name = secure_filename(self.image.filename)
        return img_name
