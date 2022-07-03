"""
    Photo_Post module
"""
from databases.managers.base import BaseManager
from databases.models.base import BaseModel


class Post(BaseModel): # pylint: disable=too-few-public-methods
    """
        Photo_Post  model class
    """
    table_name = 'Photo_Post'
    manager_class = BaseManager
