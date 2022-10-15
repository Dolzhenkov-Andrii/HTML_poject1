"""Testing suite"""
import unittest
from HTMLTestRunner.runner import HTMLTestRunner

from tests.author_test import AuthorizationTest
from tests.refresh_token_test import RefreshTokenTest

from tests.routes.posts.post_test import PostTest
from tests.routes.posts.posts_test import PostsTest
from tests.routes.posts.posts_amount_test import PostsAmountTest


suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(AuthorizationTest),
    unittest.TestLoader().loadTestsFromTestCase(RefreshTokenTest),
    unittest.TestLoader().loadTestsFromTestCase(PostTest),
    unittest.TestLoader().loadTestsFromTestCase(PostsTest),
    unittest.TestLoader().loadTestsFromTestCase(PostsAmountTest),
])

if __name__ == '__main__':

    runner = HTMLTestRunner(
        log=True,
        verbosity=2,
        output='report',
        title='Tests routes for API',
        report_name='report',
        open_in_browser=True,
        description="HTMLTestReport",
        tested_by="Dolzhenkov Andrii",
        add_traceback=False
    )

    runner.run(suite)
