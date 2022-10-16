"""Base class for Posts Test"""

from tests.test_user import TestUser
from databases.models.post import Post
from databases.models.photo import Photo
from databases.models.postStatus import PostStatus
from config.config import (
    TEST_PHOTO_PHOTO,
    TEST_POST_TITLE,
    TEST_POST_TEXT,
    TEST_STATUS_POST,
)


class TestsPosts(TestUser):
    """
        Creates test posts in the database
         to be able to test queries
    """

    def setUp(self):
        super().setUp()

        # Test post status
        post_status = PostStatus()
        post_status.name = TEST_STATUS_POST
        self.test_db.session.add(post_status)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member

        # Test photo for posts
        for i in range(1, 5):
            photo = Photo()
            photo.photo = f'{TEST_PHOTO_PHOTO}{i}'
            photo.user_id = self.user_id
            self.test_db.session.add(photo)  # pylint: disable=no-member
            self.test_db.session.commit()  # pylint: disable=no-member

        # Test posts
        post = Post()
        post.title = TEST_POST_TITLE
        post.text = TEST_POST_TEXT
        post.status_id = PostStatus.query.filter_by(
            name=TEST_STATUS_POST).first().id
        post.user_id = self.user_id
        self.test_db.session.add(post)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member
