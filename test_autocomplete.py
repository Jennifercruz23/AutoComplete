# test_autocomplete.py
"""
Tests for AutoComplete module.
"""

import unittest
from autocomplete import AutoComplete

class TestAutoComplete(unittest.TestCase):
    """Test cases for AutoComplete class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoComplete()
        self.assertIsInstance(instance, AutoComplete)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoComplete()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
