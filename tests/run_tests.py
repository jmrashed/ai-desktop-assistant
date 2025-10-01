#!/usr/bin/env python3
"""
Test runner for AI Desktop Assistant
Run all tests and generate coverage report
"""

import unittest
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def run_all_tests():
    """Discover and run all tests"""
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

def run_specific_module(module_name):
    """Run tests for a specific module"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(f'tests.{module_name}')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    print("🧪 AI Desktop Assistant Test Suite")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        module = sys.argv[1]
        print(f"Running tests for module: {module}")
        success = run_specific_module(module)
    else:
        print("Running all tests...")
        success = run_all_tests()
    
    if success:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)