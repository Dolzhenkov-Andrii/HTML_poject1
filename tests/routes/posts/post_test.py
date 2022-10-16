"""Test route post"""
from .base_class_posts import TestsPosts


class PostTest(TestsPosts):
    """posts class test"""

    URL = '/api/post'

    def test_return_post(self):
        """good post return"""
        resp = self.client.get(f'{self.URL}?id=1', headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('post', data)
        self.assertEqual(data['post'], 10)

    # def test_invalid_args(self):
    #     """Args id(int) < 0"""
    #     resp = self.client.get(f'{self.URL}?id=-4545', headers=self.access_token)
    #     self.assertEqual(resp.status_code, 200)
    #     data = resp.get_json()
    #     self.assertIn('post', data)
    #     self.assertEqual(data['post'], None)

    # def test_not_args(self):
    #     """Args id(string)"""
    #     resp = self.client.get(f'{self.URL}?id=sadsad', headers=self.access_token)
    #     self.assertEqual(resp.status_code, 200)
    #     data = resp.get_json()
    #     self.assertIn('post', data)
    #     self.assertEqual(data['post'], None)
