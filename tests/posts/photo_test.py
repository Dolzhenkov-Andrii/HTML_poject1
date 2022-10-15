"""Test route post"""
from tests.posts.base_class_posts import BasePostsTest
from databases.models.userStatus import UserStatus

class PostTest(BasePostsTest):
    """posts class test"""

    URL = '/api/status'

    def setUp(self):
        super().setUp()
        photo = UserStatus()
        photo.name = 1
        self.db.session.add(photo)
        self.db.session.commit()

    def test_photo(self):
        """good post return"""
        resp = self.client.get(f'{self.URL}/1', headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('name', data)
        self.assertEqual(data['id'], 1)
