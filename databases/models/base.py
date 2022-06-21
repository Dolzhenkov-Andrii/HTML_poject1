

class BaseModel:
    ### Использует databases.connection
    
    def __init__(self, connection, table_name):
        self.query = None
        self.connection = connection
        pass
    
    def create():
        pass

    def select(self, columns):
        columns_list = ','.join(columns)
        self.query = f"SELECT {columns_list} FROM {self.table_name}"
        return self

    def update():
        pass

    def delete():
        pass

    def join():
        pass

    def get():
        self.connection.select(self.query)

    # def join():
    #     pass