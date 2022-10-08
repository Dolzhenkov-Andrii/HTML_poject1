"""Test route posts"""
from unittest import main
import requests
from tests.posts.base_class_posts import BasePostsTest


class PostsTest(BasePostsTest):
    """posts class test"""
    route_name = 'posts'

    def test_required_token(self):
        """Route is token required"""
        resp = requests.get(self.base_url, headers={
                            'access_token': self.access_token, })
        self.assertEqual(resp.status_code, 200)

    def test_return_posts(self):
        """good post return"""
        resp = requests.get(f'{self.base_url}?position=0&amount=10', headers={
                            'access_token': self.access_token, })
        data = resp.json()
        self.assertEqual(resp.status_code, 200)
        self.assertIn('posts', data)
        self.assertEqual(len(data['posts']), 10)

    def test_request_conditions(self):
        """query condition check"""
        resp_bad = requests.get(f'{self.base_url}?position=string&amount=-10',
                                headers={'access_token': self.access_token, })
        resp_nice = requests.get(f'{self.base_url}?position=0&amount=6',
                                 headers={'access_token': self.access_token, })
        data_resp_bad = resp_bad.json()
        data_resp_nice = resp_nice.json()
        self.assertEqual(resp_bad.status_code, 200)
        self.assertEqual(resp_nice.status_code, 200)
        self.assertIn('posts', data_resp_bad)
        self.assertIn('posts', data_resp_nice)
        self.assertEqual(len(data_resp_bad['posts']), len(
            data_resp_nice['posts']))


if __name__ == '__main__':
    main()
