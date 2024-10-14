import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from data_extractor.storage.file_storage import FileStorage
from data_extractor.storage.sql_storage import SQLStorage

class TestStorage(unittest.TestCase):

    def test_file_storage(self):
        
        storage = FileStorage("test_output")
        data = "Sample text"
        storage.save(data, "test_output", "text")
        self.assertTrue(os.path.exists("test_output.txt"))

    def test_sql_storage(self):
        
        storage = SQLStorage()
        data = "Sample text 1"
        storage.store("text", data)
        self.assertTrue(os.path.exists("assignment4.db"))

    def test_file_storage_invalid_data(self):
        
        storage = FileStorage("test_output_invalid")
        data = None
        with self.assertRaises(TypeError):
            storage.save(data, "test_output", "text")

    def test_sql_storage_invalid_data(self):
        
        storage = SQLStorage()
        data = None
        with self.assertRaises(TypeError):
            storage.store("text", data)

if __name__ == '__main__':
    unittest.main()