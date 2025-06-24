import unittest
import sys
import os

# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from birthday_checker import check_birthday

class TestBirthdayChecker(unittest.TestCase):
    # Test valid inputs
    def test_valid_full_month(self):
        """Test with full month name"""
        self.assertEqual(check_birthday("13 November 1987"), (13, 11, 1987))
        
    def test_valid_month_abbreviation(self):
        """Test with month abbreviation"""
        self.assertEqual(check_birthday("13 Nov 1987"), (13, 11, 1987))
        
    def test_valid_numeric_month(self):
        """Test with numeric month"""
        self.assertEqual(check_birthday("13 11 1987"), (13, 11, 1987))
        
    # Test invalid formats
    def test_invalid_format(self):
        """Test missing components"""
        with self.assertRaises(ValueError):
            check_birthday("13 1987")
            
    def test_invalid_day_non_numeric(self):
        """Test non-numeric day"""
        with self.assertRaises(ValueError):
            check_birthday("AA November 1987")
            
    def test_invalid_month_name(self):
        """Test invalid month"""
        with self.assertRaises(ValueError):
            check_birthday("13 Novem 1987")
            
    def test_invalid_year_non_numeric(self):
        """Test non-numeric year"""
        with self.assertRaises(ValueError):
            check_birthday("13 November XXXX")
            
    def test_invalid_day_out_of_range(self):
        """Test day out of range for month"""
        with self.assertRaises(ValueError):
            check_birthday("31 February 2000")
            
    def test_invalid_year_out_of_range(self):
        """Test year out of range"""
        with self.assertRaises(ValueError):
            check_birthday("13 November 2026")
    
    # Boundary tests
    def test_earliest_valid_year(self):
        """Test earliest valid year"""
        self.assertEqual(check_birthday("01 January 1925"), (1, 1, 1925))
        
    def test_latest_valid_year(self):
        """Test latest valid year"""
        self.assertEqual(check_birthday("31 December 2025"), (31, 12, 2025))
        
    def test_below_earliest_valid_year(self):
        """Test year below range"""
        with self.assertRaises(ValueError):
            check_birthday("31 December 1924")
            
    def test_above_latest_valid_year(self):
        """Test year above range"""
        with self.assertRaises(ValueError):
            check_birthday("01 January 2026")
            
    def test_leap_year_feb_29(self):
        """Test February 29 on leap year"""
        self.assertEqual(check_birthday("29 February 2000"), (29, 2, 2000))
        
    def test_non_leap_year_feb_29(self):
        """Test February 29 on non-leap year"""
        with self.assertRaises(ValueError):
            check_birthday("29 February 1999")