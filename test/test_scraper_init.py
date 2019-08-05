import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src.scraper import WhispersScraper
from test.test_utils import TestUtils as tu
from selenium import webdriver

class TestScraperInit(unittest.TestCase):
    
    def setUp(self):
        self.scraper = WhispersScraper()

    def test_init(self):
        expected_url_type = str
        self.assertIsInstance(self.scraper._url, expected_url_type)
        
        expected_chrome_driver_type = webdriver.chrome.webdriver.WebDriver
        self.assertIsInstance(self.scraper._chrome_driver, 
                expected_chrome_driver_type)
        
        expected_post_content = {}
        self.assertEqual(self.scraper.post_content, expected_post_content)
    
    def tearDown(self):
        self.scraper._chrome_driver.quit()

if __name__ == '__main__':
    unittest.main()

