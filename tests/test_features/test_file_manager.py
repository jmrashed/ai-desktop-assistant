import unittest
from unittest.mock import patch, mock_open
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.features.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    
    def setUp(self):
        self.file_manager = FileManager()
    
    @patch('os.walk')
    def test_search_files_found(self, mock_walk):
        mock_walk.return_value = [
            ('/test', [], ['test.txt', 'document.pdf']),
            ('/test/sub', [], ['test2.txt'])
        ]
        
        result = self.file_manager.search_files('test')
        self.assertIn("Found 2 files", result)
        self.assertIn("test.txt", result)
    
    @patch('os.walk')
    def test_search_files_not_found(self, mock_walk):
        mock_walk.return_value = [('/test', [], ['document.pdf'])]
        
        result = self.file_manager.search_files('nonexistent')
        self.assertIn("No files found", result)
    
    @patch('os.makedirs')
    def test_create_folder_success(self, mock_makedirs):
        result = self.file_manager.create_folder('TestFolder')
        mock_makedirs.assert_called_once_with('TestFolder', exist_ok=True)
        self.assertIn("created successfully", result)
    
    @patch('os.makedirs')
    def test_create_folder_error(self, mock_makedirs):
        mock_makedirs.side_effect = Exception("Permission denied")
        
        result = self.file_manager.create_folder('TestFolder')
        self.assertIn("Error creating folder", result)
    
    @patch('os.walk')
    def test_search_files_error(self, mock_walk):
        mock_walk.side_effect = Exception("Access denied")
        
        result = self.file_manager.search_files('test')
        self.assertIn("Error searching files", result)

if __name__ == '__main__':
    unittest.main()