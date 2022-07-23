"""
    Base meta module for models
"""
from databases.managers.base import BaseManager


class MetaModel(type):
    """
        Base meta class for models
    """
    manager_class = BaseManager

    def _get_manager(cls):
        return cls.manager_class(model_class=cls)

    @property
    def objects(cls):
        """
            .objects property
        """
        return cls._get_manager()
