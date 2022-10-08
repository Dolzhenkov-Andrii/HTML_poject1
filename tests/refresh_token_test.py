"""Test route refresh_token"""
from unittest import TestCase, main
import requests




class RefreshTokenTest(TestCase):
    """refresh_token class test"""
    URL = 'http://127.0.0.1:5050/api/refresh_token'

    def test_not_404(self):
        """Route exists"""
        resp = requests.get(self.URL)
        self.assertNotEqual(resp.status_code, 404)

    def test_1(self):
        """test 1"""
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 400)


if __name__=='__main__':
    main()
