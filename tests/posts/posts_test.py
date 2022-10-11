"""Test route posts"""
from tests.posts.base_class_posts import BasePostsTest


class PostsTest(BasePostsTest):
    """posts class test"""

    URL = '/api/posts'

    def test_return_posts(self):
        """good post return"""
        resp = self.client.get(f'{self.URL}?position=0&amount=10', headers=self.access_token)
        data = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertIn('posts', data)
        self.assertEqual(len(data['posts']), 10)

    def test_request_conditions(self):
        """query condition check"""
        resp_bad = self.client.get(f'{self.URL}?position=string&amount=-10',
                                headers=self.access_token)
        resp_nice = self.client.get(f'{self.URL}?position=0&amount=6',
                                 headers=self.access_token)
        self.assertEqual(resp_bad.status_code, 200)
        self.assertEqual(resp_nice.status_code, 200)
        data_resp_bad = resp_bad.get_json()
        data_resp_nice = resp_nice.get_json()
        self.assertIn('posts', data_resp_bad)
        self.assertIn('posts', data_resp_nice)
        self.assertEqual(len(data_resp_bad['posts']), len(
            data_resp_nice['posts']))
