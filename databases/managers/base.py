"""
    BaseManager
"""

class BaseManager:
    """
        Base manager
    """
    database_connection = {}

    def __init__(self, model_class):
        self.query = None
        self.model_class = model_class
        connection = BaseManager.database_connection
        self.cursor = connection.cursor() # pylint: disable=no-member

#select column_name from information_schema.columns where table_name = 'Post' and  table_schema = 'my_blog'
# Закінчи метотд def get_date(self): повинен повертати обект або обєкти вже з данними із ДБ
    @property
    def get_date(self):
        """
            To get data
        """
        with self.cursor as cursor:
            print(self.query)
            cursor.execute(self.query)
            result = [item for item in cursor]
            model_objects = []
            for row_values in result:
                keys, values = row_values, row_values.values()
                row_data = dict(zip(keys, values))
                model_objects.append(self.model_class(**row_data))
            return model_objects

    def select(self, *field_names):
        """
            Select field using names
        """

        fields_format = ', '.join(field_names)
        self.query  = f"SELECT {fields_format} FROM {self.model_class.table_name} "
        return self

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

    def all(self):
        """
            Select All items
        """

        if self.query:
            self.select('*')
        return self.get_date

    def first(self, colum_name='id'):
        """
            Select first item
        """

        if self.query:
            self.select('*')
        self.query += f'order by {colum_name} asc limit 1'
        return self.get_date

    def last(self, colum_name='id'):
        """
            Select last item
        """

        if self.query:
            self.select('*')
        self.query += f'order by {colum_name} desc limit 1'
        return self.get_date

    def limit(self, size=100):
        """
            Limit items from select
        """

        if self.query:
            self.select('*')
        self.query += f'limit {size}'
        return self.get_date

    def offset(self, args):
        """
            Offset items from select
        """

        if self.query:
            self.select('*')
        self.query += 'limit ' + args
        return self.get_date
