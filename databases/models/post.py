"""
    Post module
"""
from databases.managers.base import BaseManager
from databases.models.base import BaseModel


class Post(BaseModel): # pylint: disable=too-few-public-methods
    """
        Post model class
    """
    table_name = 'post'
    manager_class = BaseManager
    foreign_keys = {
        'photo_posts': 'post_id'
    }
    
    def photo_posts(self):
        """
            Getting many-to-many photos
        """
        # PhotoPost
        # 
        return PhotoPost.objects.filter(post_id=self.primary_key)

    
    def prefetch():
        # JOIN
        pass


class PhotoPost:

    @property
    def post(cls):
        return Post

    @property
    def photo(cls):
        return Photo.objects.get(id=self.photo_id)


## select -> 
    # 1. all
    # 2. first 
    # 3. last
# 4. limit
# 5. offset


## filter -> sql WHERE 

Post.objects.first().photo_posts().first().photo -> Manager -> all, first, last -> filter




Post.objects.where(id=10).photos().values('photo')
PhotoPost.objects.all() -> # SELECT * FROM photo_post -> [PhotoPost, PhotoPost]
PhotoPost.objects.all().values('photo') -> # [Photo, Photo]
PhotoPost.objects.all().values('post') -> # [Post, Post]


photo_post = PhotoPost.objects.first()
post = photo_post.post -> Post
photo = photo_post.photo -> Photo