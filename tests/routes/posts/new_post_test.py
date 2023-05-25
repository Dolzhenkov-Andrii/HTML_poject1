"""Test route new post"""


from .base_class_posts import TestsPosts

class NewPostTest(TestsPosts):
    """Class tests new post"""

    URL = '/api/new-post'


    def test_creat_new_post(self):
        """Now test logic"""

        test_form = {
            'title': 'Hellow',
            'text': 'World',
        }

        resp = self.client.post(self.URL, json=test_form, headers=self.access_token)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, '123')
