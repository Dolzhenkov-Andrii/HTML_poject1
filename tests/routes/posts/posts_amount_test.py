"""Test route posts_amount"""
from tests.posts.base_class_posts import BasePostsTest

class PostsAmountTest(BasePostsTest):
    """posts_amount class test"""

    URL = '/api/posts_amount'

    def test_response_size(self):
        """Route response amount posts"""
        resp = self.client.get(self.URL, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertGreaterEqual(data['size'], 0)
