"""Test route posts_amount"""
from unittest import main
import requests
from tests.posts.base_class_posts import BasePostsTest

class PostsAmountTest(BasePostsTest):
    """posts_amount class test"""
    route_name = 'posts_amount'

    def test_not_404(self):
        """Route exists"""
        resp = requests.get(self.base_url)
        self.assertNotEqual(resp.status_code, 404)

    def test_required_token(self):
        """Route is token required"""
        resp = requests.get(self.base_url, headers={'access_token': self.access_token, })
        self.assertEqual(resp.status_code, 200)

    def test_response_size(self):
        """Route response amount posts"""
        resp = requests.get(self.base_url, headers={'access_token': self.access_token, })
        data = resp.json()
        self.assertGreaterEqual(data['size'], 0)


if __name__ == '__main__':
    main()
