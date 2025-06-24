import unittest
import sys
import os

# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from color_finder import find_lucky_color

class TestColorFinder(unittest.TestCase):
    # Test regular numbers
    def test_regular_number(self):
        """Regular number mapping"""
        self.assertEqual(find_lucky_color(5), "Sky Blue")
        
    def test_master_number_11(self):
        """Master number 11 mapping"""
        self.assertEqual(find_lucky_color(11), "Silver")
        
    def test_master_number_22(self):
        """Master number 22 mapping"""
        self.assertEqual(find_lucky_color(22), "White")
        
    def test_master_number_33(self):
        """Master number 33 mapping"""
        self.assertEqual(find_lucky_color(33), "Crimson")
        
    def test_all_regular_numbers(self):
        """Test all regular number mappings"""
        expected_colors = {
            1: "Red", 2: "Orange", 3: "Yellow", 4: "Green",
            5: "Sky Blue", 6: "Indigo", 7: "Violet", 
            8: "Magenta", 9: "Gold"
        }
        for number, color in expected_colors.items():
            self.assertEqual(find_lucky_color(number), color)
            
    def test_invalid_number(self):
        """Test invalid life path number"""
        with self.assertRaises(ValueError):
            find_lucky_color(10)
            
    def test_invalid_number_zero(self):
        """Test zero as invalid"""
        with self.assertRaises(ValueError):
            find_lucky_color(0)