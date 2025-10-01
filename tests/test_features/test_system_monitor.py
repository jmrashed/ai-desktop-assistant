import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.features.system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    
    def setUp(self):
        self.monitor = SystemMonitor()
    
    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.disk_usage')
    def test_get_system_info_success(self, mock_disk, mock_memory, mock_cpu):
        mock_cpu.return_value = 50.0
        
        mock_memory_obj = MagicMock()
        mock_memory_obj.percent = 60.0
        mock_memory.return_value = mock_memory_obj
        
        mock_disk_obj = MagicMock()
        mock_disk_obj.percent = 70.0
        mock_disk.return_value = mock_disk_obj
        
        result = self.monitor.get_system_info()
        self.assertIn("CPU: 50.0%", result)
        self.assertIn("Memory: 60.0%", result)
        self.assertIn("Disk: 70.0%", result)
    
    @patch('psutil.cpu_percent')
    def test_get_system_info_error(self, mock_cpu):
        mock_cpu.side_effect = Exception("System error")
        
        result = self.monitor.get_system_info()
        self.assertIn("Error getting system info", result)

if __name__ == '__main__':
    unittest.main()