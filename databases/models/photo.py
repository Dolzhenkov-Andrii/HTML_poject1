"""
    Photo module
"""
from databases.managers.base import BaseManager
from databases.models.base import BaseModel


class Photo(BaseModel): # pylint: disable=too-few-public-methods
    """
        Photo model class
    """
    table_name = 'User_Photo'
    manager_class = BaseManager
