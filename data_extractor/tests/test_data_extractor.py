import sys
import os

from data_extractor.data_extractor.pdf_extractor import PDFExtractor
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from data_extractor.file_loaders.pdf_loader import PDFLoader

class TestDataExtractor(unittest.TestCase):

    def test_extract_data(self):
        
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = extractor.extract_data("../files/sample.pdf")
        self.assertIsInstance(data, list)

    def test_extract_data_empty_file(self):
        
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = extractor.extract_data("./files/empty.pdf")
        self.assertEqual(data, [])

    def test_extract_data_invalid_file(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        with self.assertRaises(FileNotFoundError):
            extractor.extract_data("./files/non_existent_file.pdf")

if __name__ == '__main__':
    unittest.main()