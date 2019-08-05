import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src.data_saver import DataSaver

class TestScraperUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ds = DataSaver()
    
    def test_create_empty_text_file(self):
        self.ds.create_empty_text_file()
        self.assertTrue(os.path.isfile('output.txt'))
    
    def test_append_to_text_file(self):
        input_text = 'Example Text'
        self.ds.append_to_text_file(input_text)
        output_text = ''
        with open('output.txt', 'r', encoding='utf-8') as f:
            output_text = f.read()
        self.assertEqual(input_text, output_text)

    @classmethod
    def tearDownClass(cls):
        os.remove('output.txt')

if __name__ == '__main__':
    unittest.main()

