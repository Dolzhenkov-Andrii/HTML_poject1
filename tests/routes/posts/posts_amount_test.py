"""
    Test route posts_amount
"""

from tests.test_user import TestUser
from databases.models.post import Post
from databases.models.photo import Photo
from databases.models.postStatus import PostStatus
from config.config import (
    TEST_PHOTO_PHOTO,
    TEST_POST_TITLE,
    TEST_POST_TEXT,
    TEST_STATUS_POST,
    TEST_POST_COUNT,
)


class PostsAmountTest(TestUser):
    """
        posts_amount class test
    """

    URL = '/api/posts_amount'

    def test_none_response(self):
        """
            Test response zero posts
        """
        resp = self.client.get(self.URL, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertGreaterEqual(data['size'], 0)

    def test_size_response(self):
        """
            Test response amount posts
        """
        # Test post status
        post_status = PostStatus()
        post_status.name = TEST_STATUS_POST
        self.test_db.session.add(post_status)  # pylint: disable=no-member
        self.test_db.session.commit()  # pylint: disable=no-member
        test_size = range(1, TEST_POST_COUNT)
        for number_post in test_size:
            # Test photo for posts
            photo = Photo()
            photo.photo = f'{TEST_PHOTO_PHOTO}{number_post}'
            photo.user_id = self.user_id

            # Test posts
            post = Post()
            post.title = f'{TEST_POST_TITLE} {number_post}'
            post.text = TEST_POST_TEXT
            post.status_id = PostStatus.query.filter_by(
                name=TEST_STATUS_POST).first().id
            post.user_id = self.user_id
            post.photos = [photo]
            self.test_db.session.add(photo)  # pylint: disable=no-member
            self.test_db.session.add(post)  # pylint: disable=no-member
            self.test_db.session.commit()  # pylint: disable=no-member

        resp = self.client.get(self.URL, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data['size'], len(test_size))
