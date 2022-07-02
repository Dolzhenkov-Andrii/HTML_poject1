"""
    Base model module
"""
from databases.models.meta import MetaModel

class BaseModel(metaclass=MetaModel): # pylint: disable=too-few-public-methods
    """
        BaseModel for our models
    """
    table_name = ""
    primary_key = "id"
    foreign_keys = {}
