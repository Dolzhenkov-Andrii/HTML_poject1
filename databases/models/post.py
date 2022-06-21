from databases.models import BaseModel


class Post(BaseModel):
    table_name = 'posts'
    ### Использует методы с BaseModel
    
    def __init__(self, connection, table_name):
        super().__init__(connection, Post.table_name)