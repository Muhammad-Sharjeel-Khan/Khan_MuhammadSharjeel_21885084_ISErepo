import unittest
import sys
import os

# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from life_path_calculator import calculate_life_path_number

class TestLifePathCalculator(unittest.TestCase):
    # Basic calculation tests
    def test_basic_calculation(self):
        """Basic calculation with single-digit result"""
        self.assertEqual(calculate_life_path_number(1, 1, 2000), 4)
        
    def test_reduction_needed(self):
        """Calculation with reduction needed"""
        self.assertEqual(calculate_life_path_number(29, 8, 1994), 6)
        
    def test_master_number_result(self):
        """Calculation with master number result"""
        self.assertEqual(calculate_life_path_number(29, 2, 1980), 22)
        
    def test_master_number_input(self):
        """Calculation with master number input"""
        self.assertEqual(calculate_life_path_number(11, 3, 1986), 2)
        
    def test_multiple_master_numbers(self):
        """Calculation with multiple master numbers"""
        self.assertEqual(calculate_life_path_number(11, 11, 2000), 6)
    
    # White-box tests
    def test_single_digit_path(self):
        """Single-digit number path"""
        self.assertEqual(calculate_life_path_number(1, 1, 2000), 4)
        
    def test_master_number_input_path(self):
        """Master number input path"""
        self.assertEqual(calculate_life_path_number(11, 5, 2000), 9)
        
    def test_master_number_output_path(self):
        """Master number output path"""
        self.assertEqual(calculate_life_path_number(29, 2, 1980), 22)
        
    def test_recursive_addition_path(self):
        """Recursive digit addition path"""
        self.assertEqual(calculate_life_path_number(29, 12, 1994), 1)
        
    def test_multiple_masters_input_path(self):
        """Multiple master numbers input"""
        self.assertEqual(calculate_life_path_number(11, 22, 1987), 4)