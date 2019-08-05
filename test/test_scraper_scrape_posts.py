import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src.scraper import WhispersScraper
from test.test_utils import TestUtils as tu
from src.duplicate_post_idx_exception import DuplicatePostIdxException

class TestScraperScrapePosts(unittest.TestCase):
    
    def setUp(self):
        self.maxDiff = None
        self.scraper = WhispersScraper()
    
    def test_scrape_valid_idx(self):
        start_idx = tu.VALID_POST_67234_IDX
        end_idx = tu.VALID_POST_67234_IDX
        self.scraper.scrape_posts(start_idx, end_idx)
        expected_post_content = \
                {tu.VALID_POST_67234_IDX:tu.VALID_POST_67234_TEXT}
        self.assertEqual(self.scraper.post_content, expected_post_content)

    def test_scrape_valid_idx_with_link(self):
        start_idx = tu.VALID_POST_67213_IDX
        end_idx = tu.VALID_POST_67213_IDX
        self.scraper.scrape_posts(start_idx, end_idx)
        expected_post_content = \
                {tu.VALID_POST_67213_IDX:tu.VALID_POST_67213_TEXT}
        self.assertEqual(self.scraper.post_content, expected_post_content)

    def test_scrape_invalid_idx(self):
        start_idx = tu.INVALID_POST_67232_IDX
        end_idx = tu.INVALID_POST_67232_IDX
        self.scraper.scrape_posts(start_idx, end_idx)
        expected_post_content = {}
        self.assertEqual(self.scraper.post_content, expected_post_content) 
    '''
    def test_scrape_raise_DuplicatePostIdxException(self):
        start_idx = tu.VALID_POST_67213_IDX
        end_idx = tu.VALID_POST_67213_IDX
        self.scraper.scrape_posts(start_idx, end_idx)
        
        with self.assertRaises(DuplicatePostIdxException) as ex:
            self.scraper.scrape_posts(start_idx, end_idx)
    '''
    def tearDown(self):
        self.scraper._chrome_driver.quit()

if __name__ == '__main__':
    unittest.main()

