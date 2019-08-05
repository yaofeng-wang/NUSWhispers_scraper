import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src.scraper import WhispersScraper
from test.test_utils import TestUtils as tu

class TestScraperGetContents(unittest.TestCase):

    def setUp(self):
        self.scraper = WhispersScraper()

    def test_get_post_content(self):
        test_html = ''
        with open(tu.VALID_POST_67213_HTML_DIR, 'r', encoding = 'utf-8') as f:
            test_html += f.read()
            f.close()
        actual_post_text = self.scraper._get_post_contents(test_html)
        expected_post_text = tu.VALID_POST_67213_TEXT
        self.assertEqual(actual_post_text, expected_post_text)

    def tearDown(self):
        self.scraper._chrome_driver.quit()
    
if __name__ == '__main__':
    unittest.main()

