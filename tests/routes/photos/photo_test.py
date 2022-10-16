"""Test route post"""
from tests.test_user import TestUser
from databases.models.photo import Photo
from config.config import TEST_PHOTO_PHOTO

class PhotoTest(TestUser):
    """Photo class test"""

    URL = '/api/photo'

    def setUp(self):
        super().setUp()
        for i in range(1,11):
            photo = Photo()
            photo.photo = f'{TEST_PHOTO_PHOTO}{i}'
            photo.user_id = self.user_id
            self.test_db.session.add(photo) # pylint: disable=no-member
            self.test_db.session.commit() # pylint: disable=no-member

    def test_photo(self):
        """good post return"""
        photo_id = 4
        resp = self.client.get(f'{self.URL}?id={photo_id}', headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('photo', data)
        self.assertEqual(data['photo']['id'], photo_id)
        self.assertEqual(data['photo']['photo'], f'{TEST_PHOTO_PHOTO}{photo_id}')

    def test_invalid_query_int(self):
        """
            Invalid query string where id= int < 0
            must return None
        """
        resp = self.client.get(f'{self.URL}?id=-1', headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('photo', data)
        self.assertEqual(data['photo'], None)

    def test_invalid_query_str(self):
        """
            Invalid query string where id= str
            must return None
        """
        resp = self.client.get(f'{self.URL}?id=test', headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('photo', data)
        self.assertEqual(data['photo'], None)

    def test_invalid_query_none(self):
        """
            Invalid query string where not request.args
            must return None
        """
        resp = self.client.get(self.URL, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('photo', data)
        self.assertEqual(data['photo'], None)
