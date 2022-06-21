from databases.models import BaseModel


class Photo(BaseModel):
    table_name = 'photo'
    ### Использует методы с BaseModel
    
    def __init__(self, connection, table_name):
        super().__init__(connection, Photo.table_name)