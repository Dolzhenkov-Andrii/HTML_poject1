"""
    Post module
"""
from databases.managers.base import BaseManager
from databases.models.base import BaseModel
from databases.models.postphoto import PhotoPost
from databases.models.photo import Photo


class Post(BaseModel):
    """
        Post model class
    """
    table_name = 'Post'
    manager_class = BaseManager
    photo = None
    id = None

    def photo_posts(self):
        """
            Getting many-to-many photos
        """
        id_photo = PhotoPost.objects.filters('post_id',self.id).get_date[0]
        self.photo = Photo.objects.filters(
            'id',f'{id_photo.photo_id}').get_date[0].photo
        return self
        # PhotoPost
        # return PhotoPost.objects.filter(post_id=getattr(self, self.primary_key))


    # def prefetch():
    #     # JOIN
    #     pass



# class PhotoPost:
#     post = ForeignKey(Post, 'post_id', 'id')
#     photo = ForeignKey(Photo, 'post_id', 'id')

#     @property
#     def post(cls):
#         return Post

#     @property
#     def photo(cls):
#         return Photo.objects.get(id=self.photo_id)



## select ->
    # 1. all
    # 2. first
    # 3. last
# 4. limit
# 5. offset

# Post.objects.prefetch('photo_posts').photo_posts.prefetch('photo').first().photo

## filter -> sql WHERE

# Post.objects.first().photo_posts().first().photo -> Manager -> all, first, last -> filter




# Post.objects.where(id=10).photos().values('photo')
# PhotoPost.objects.all() -> # SELECT * FROM photo_post -> [PhotoPost, PhotoPost]
# PhotoPost.objects.all().values('photo') -> # [Photo, Photo]
# PhotoPost.objects.all().values('post') -> # [Post, Post]


# photo_post = PhotoPost.objects.first()
# post = photo_post.post -> Post
# photo = photo_post.photo -> Photo
