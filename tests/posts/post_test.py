"""Test route post"""
from unittest import main
import requests
from tests.posts.base_class_posts import BasePostsTest


class PostTest(BasePostsTest):
    """posts class test"""
    route_name = 'post'

    def test_not_404(self):
        """Route exists"""
        resp = requests.get(self.base_url)
        self.assertNotEqual(resp.status_code, 404)

    def test_required_token(self):
        """Route is token required"""
        resp = requests.get(f'{self.base_url}?id=0', headers={'access_token': self.access_token, })
        self.assertEqual(resp.status_code, 200)

    def test_return_post(self):
        """good post return"""
        resp = requests.get(f'{self.base_url}?id=10', headers={
                            'access_token': self.access_token, })
        data = resp.json()
        self.assertEqual(resp.status_code, 200)
        self.assertIn('post', data)
        self.assertEqual(data['post']['id'], 10)

    def test_invalid_args(self):
        """Args id(int) < 0"""
        resp = requests.get(f'{self.base_url}?id=-4545', headers={
                            'access_token': self.access_token, })
        data = resp.json()
        self.assertEqual(resp.status_code, 200)
        self.assertIn('post', data)
        self.assertEqual(data['post'], None)

    def test_not_args(self):
        """Args id(string)"""
        resp = requests.get(f'{self.base_url}?id=sadsad', headers={
                            'access_token': self.access_token, })
        data = resp.json()
        self.assertEqual(resp.status_code, 200)
        self.assertIn('post', data)
        self.assertEqual(data['post'], None)

if __name__ == '__main__':
    main()
