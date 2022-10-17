"""Test route post"""

from config.config import (
    TEST_PHOTO_PHOTO,
    TEST_USER_USERNAME,
    TEST_POST_COUNT,
    TEST_POST_TITLE
    )
from exceptions.posts import PostArgsError
from .base_class_posts import TestsPosts

class PostTest(TestsPosts):
    """posts class test"""

    URL = '/api/post'

    def test_return_post(self):
        """
            Validates the returned POST
            and all required fields in the POST,
            including the user
            and photos associated with them
        """
        for number_post in range(1, TEST_POST_COUNT):
            resp = self.client.get(f'{self.URL}?id={number_post}', headers=self.access_token)
            self.assertEqual(resp.status_code, 200)
            data = resp.get_json()
            #Checking if a field exists
            self.assertIn('post', data)
            self.assertIn('id',data['post'])
            self.assertIn('title',data['post'])
            self.assertIn('creation_date',data['post'])
            self.assertIn('text',data['post'])
            self.assertIn('likes',data['post'])
            self.assertIn('view',data['post'])
            self.assertIn('shared',data['post'])
            self.assertIn('status',data['post'])
            self.assertIn('user',data['post'])
            self.assertIn('photos',data['post'])
            #Checking if a value exists
            self.assertEqual(data['post']['id'], number_post)
            self.assertEqual(data['post']['title'], f'{TEST_POST_TITLE} {number_post}')
            self.assertEqual(data['post']['user']['username'], TEST_USER_USERNAME)
            self.assertEqual(data['post']['photos'][0]['photo'], f'{TEST_PHOTO_PHOTO}{number_post}')


    def test_invalid_args(self):
        """Args id(int) < 0"""
        resp = self.client.get(f'{self.URL}?id=-4545', headers=self.access_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, PostArgsError.message)

    def test_not_args(self):
        """Args id(string)"""
        resp = self.client.get(f'{self.URL}?id=sadsad', headers=self.access_token)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, PostArgsError.message)
