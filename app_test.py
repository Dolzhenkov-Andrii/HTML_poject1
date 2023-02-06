'''Testing suite'''

import unittest
from HTMLTestRunner.runner import HTMLTestRunner

from tests.token_required_test import TokenRequiredTest
from tests.routes.refresh_token_test import RefreshTokenTest
from tests.routes.author_test import AuthorizationTest
from tests.routes.registr_test import RegistrationTest
from tests.routes.photos.photo_test import PhotoTest
from tests.routes.posts.posts_amount_test import PostsAmountTest
from tests.routes.posts.posts_test import PostsTest
from tests.routes.posts.post_test import PostTest


suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(TokenRequiredTest),
    unittest.TestLoader().loadTestsFromTestCase(RefreshTokenTest),
    unittest.TestLoader().loadTestsFromTestCase(AuthorizationTest),
    unittest.TestLoader().loadTestsFromTestCase(RegistrationTest),
    unittest.TestLoader().loadTestsFromTestCase(PhotoTest),
    unittest.TestLoader().loadTestsFromTestCase(PostsAmountTest),
    unittest.TestLoader().loadTestsFromTestCase(PostsTest),
    unittest.TestLoader().loadTestsFromTestCase(PostTest),
])

if __name__ == '__main__':

    runner = HTMLTestRunner(
        log=True,
        verbosity=2,
        output='report',
        title='Tests routes for API',
        report_name='report',
        open_in_browser=True,
        description='HTMLTestReport',
        tested_by='Dolzhenkov Andrii',
        add_traceback=True
    )

    runner.run(suite)
