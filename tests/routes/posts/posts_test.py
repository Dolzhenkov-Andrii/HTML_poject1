"""Test route posts"""
from config.config import BASE_COUNT_POSTS, BASE_POSITION_POSTS, TEST_POST_COUNT
from .base_class_posts import TestsPosts
from exceptions.posts import PostArgsError


class PostsTest(TestsPosts):
    """posts class test"""

    URL = '/api/posts'

    def test_return_posts(self):
        """good post return"""
        resp = self.client.get(
            f'{self.URL}?position={BASE_POSITION_POSTS}&amount={BASE_COUNT_POSTS}',
            headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('posts', data)
        self.assertEqual(len(data['posts']), BASE_COUNT_POSTS)

    def test_invalid_position_int(self):
        """
            Invalid query string where ?position=(int < 0)&amount=int
            must return message:'Request arguments error'
        """
        test_position = -5
        resp = self.client.get(
            f'{self.URL}?position={test_position}&amount={BASE_COUNT_POSTS}',
            headers=self.access_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, PostArgsError.message)

    def test_invalid_amount_int(self):
        """
            Invalid query string where ?position=int&amount=(int < 0)
            must return message:'Request arguments error'
        """
        test_amount = -5
        resp = self.client.get(
            f'{self.URL}?position={BASE_POSITION_POSTS}&amount={test_amount}',
            headers=self.access_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, PostArgsError.message)

    def test_invalid_position_str(self):
        """
            Invalid query string where ?position=str&amount=int
            must return default ?position=0&amount=6
        """
        test_position = 'test'
        resp = self.client.get(
            f'{self.URL}?position={test_position}&amount={BASE_COUNT_POSTS}',
            headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('posts', data)
        self.assertEqual(len(data['posts']), BASE_COUNT_POSTS)

    def test_invalid_amount_str(self):
        """
            Invalid query string where ?position=int&amount=str
            must return default ?position=0&amount=6
        """
        test_amount = 'test'
        resp = self.client.get(
            f'{self.URL}?position={BASE_POSITION_POSTS}&amount={test_amount}',
            headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('posts', data)
        self.assertEqual(len(data['posts']), BASE_COUNT_POSTS)


    def test_invalid_query_none(self):
        """
            Invalid query string where not request.args
            must return default ?position=0&amount=6
        """
        resp = self.client.get(self.URL, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('posts', data)
        self.assertEqual(len(data['posts']), BASE_COUNT_POSTS)
