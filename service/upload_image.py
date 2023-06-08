"""Upload Image
"""

import os
import time
from config.config import UPLOAD_FOLDER
from validations.image_valid import ImageValidName
from exceptions.validate import InvalidImage

class UploadImage:
    """ save Img on server
    """

    def __init__(self, image=None):
        self.image = image
        self.filename = ''

    def save_image(self) -> str:
        """ save Img and return img name
        """
        if self.image and self.image.filename != '':
            self.filename = f'{int(time.time())*1000}'
            try:
                self.filename += ImageValidName(self.image).validate()
            except InvalidImage as error:
                raise error
            self.image.save(os.path.join(UPLOAD_FOLDER, self.filename))
        return self.filename
