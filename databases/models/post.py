from databases.models.base import BaseModel


# print(BaseModel(connection,'Photo_Post').select('Post.id', 'Post.title', 'User_Photo.photo').join('JOIN','Post','Post.id','Photo_Post.post_id').join('JOIN', 'User_Photo', 'Photo_Post.photo_id','User_Photo.id').limit(6).get())


class Post(BaseModel):
    table_name = 'Post'
    ### Использует методы с BaseModel
    def __init__(self, connection):
        super().__init__(connection)
        
        
    def getPost(self, limit, sort=None):
        table_name = 'Photo_Post'
        self._select(table_name,'Post.id', 'Post.title','Post.text', 'User_Photo.photo')
        self._join('JOIN','Post','Post.id','Photo_Post.post_id')
        self._join('JOIN', 'User_Photo', 'Photo_Post.photo_id','User_Photo.id')
        self._sort(sort)._limit(limit)
        return self._get()
    #Base!!!!
    def lenPost(self):
        return len(self._select(self.table_name,'id')._get())
    #Photo
    def updatePost(self, *value, condition=None):
        if 'photo' in ' '.join(value):
            self.table_name = 'User_Photo'
        return self._update(self.table_name,condition,*value)._get()
    
    
