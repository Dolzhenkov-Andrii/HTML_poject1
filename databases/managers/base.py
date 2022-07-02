"""
    BaseManager
"""

from unittest import result


class BaseManager:
    """
        Base manager
    """
    database_connection = {}
   
    def __init__(self, model_class):
        self.model_class = model_class
        connection = BaseManager.database_connection
        self.cursor = connection.cursor() # pylint: disable=no-member

    def select(self, *field_names):
        """
            Select field using names
        """

        fields_format = ', '.join(field_names)
        query = f"SELECT {fields_format} FROM {self.model_class.table_name}"

    def bulk_insert(self, rows: list):
        """
            Multiple insert
        """

    def update(self, new_data: dict):
        """
            Update data from dictionary - new_data
        """

    def delete(self):
        """
            SQL DELETE
        """
