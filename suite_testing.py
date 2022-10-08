"""Testing suite"""
import unittest

from HTMLTestRunner.runner import HTMLTestRunner

from tests.author_test import AuthorizationTest
from tests.refresh_token_test import RefreshTokenTest

from tests.posts.post_test import PostTest
from tests.posts.posts_test import PostsTest
from tests.posts.posts_amount_test import PostsAmountTest

test1 = unittest.TestLoader().loadTestsFromTestCase(AuthorizationTest)
test2 = unittest.TestLoader().loadTestsFromTestCase(RefreshTokenTest)
test3 = unittest.TestLoader().loadTestsFromTestCase(PostTest)
test4 = unittest.TestLoader().loadTestsFromTestCase(PostsTest)
test5 = unittest.TestLoader().loadTestsFromTestCase(PostsAmountTest)
suite = unittest.TestSuite([test1, test2, test3, test4, test5])

if __name__ == '__main__':

    runner = HTMLTestRunner(
        log=True,
        verbosity=2,
        output='report',
        title='Tests routes for API',
        report_name='report',
        open_in_browser=True,
        description="HTMLTestReport",
        tested_by="Ravikirana B",
        add_traceback=False
        )

    runner.run(suite)
