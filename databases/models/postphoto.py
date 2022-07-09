"""
    Photo_Post module
"""
# from databases.models.photo import Photo
# from databases.models.post import Post            !!!???
from databases.managers.base import BaseManager
from databases.models.base import BaseModel


class PhotoPost(BaseModel):
    """
        Photo_Post  model class
    """
    table_name = 'Photo_Post'
    manager_class = BaseManager
    photo_id = ''
    post_id = ''
    # post = None
    # photo = None

    # @property
    # def photo_posts(self):
    #     """
    #         Select two objects Photo and Post
    #     """
    #     self.post = Post.objects.filters(
    #         self.photo_id, f'{Post.table_name}.id').get_date[0]  # pylint: disable=no-member
    #     self.photo = Photo.objects.filters(
    #         self.photo_id, f'{Photo.table_name}.id').get_date[0]  # pylint: disable=no-member
    #     return self
