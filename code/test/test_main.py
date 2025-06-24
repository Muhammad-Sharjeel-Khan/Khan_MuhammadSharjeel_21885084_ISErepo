import unittest
import io
import sys
import os
from unittest.mock import patch

# Add the parent directory to Python path to import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

import main
from birthday_checker import check_birthday
from life_path_calculator import calculate_life_path_number
from color_finder import find_lucky_color
from generation_finder import find_generation

class TestMainProgram(unittest.TestCase):
    @patch('builtins.input', return_value='13 November 1987')
    def test_valid_input(self, mock_input):
        """Test with valid birthday input"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Simulate the main program flow
        birthday = mock_input()
        day, month, year = check_birthday(birthday)
        lpn = calculate_life_path_number(day, month, year)
        color = find_lucky_color(lpn)
        gen = find_generation(year)
        
        # Print output like main program does
        print(f"\nYour birthday : {birthday}")
        print(f"Your life path number : {lpn}")
        print(f"Your lucky color : {color}")
        print(f"Your generation : {gen}")
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("13 November 1987", output)
        self.assertIn("Your life path number", output)
        self.assertIn("Your lucky color", output)
        self.assertIn("Your generation", output)
        
    @patch('builtins.input', return_value='13 XX 1987')
    def test_invalid_input(self, mock_input):
        """Test with invalid birthday input"""
        with self.assertRaises(ValueError):
            birthday = mock_input()
            day, month, year = check_birthday(birthday)
            
    def test_integration_example_1(self):
        """Test full integration with example data"""
        # Test the 3179 from student ID
        day, month, year = check_birthday("31 July 1979")
        lpn = calculate_life_path_number(day, month, year)
        color = find_lucky_color(lpn)
        gen = find_generation(year)
        
        self.assertEqual((day, month, year), (31, 7, 1979))
        self.assertEqual(gen, "Generation X")
        
    def test_integration_example_2(self):
        """Test with Khan surname related date"""
        day, month, year = check_birthday("15 August 1990")
        lpn = calculate_life_path_number(day, month, year)
        color = find_lucky_color(lpn)
        gen = find_generation(year)
        
        self.assertEqual((day, month, year), (15, 8, 1990))
        self.assertEqual(gen, "Millennials")