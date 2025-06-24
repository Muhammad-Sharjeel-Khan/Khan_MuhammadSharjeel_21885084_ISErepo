import unittest
import sys
import os

# Add the source directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from generation_finder import find_generation

class TestGenerationFinder(unittest.TestCase):
    # Test each generation
    def test_silent_generation(self):
        """Silent Generation year"""
        self.assertEqual(find_generation(1940), "Silent Generation")
        
    def test_baby_boomers(self):
        """Baby Boomers year"""
        self.assertEqual(find_generation(1960), "Baby Boomers")
        
    def test_generation_x(self):
        """Generation X year"""
        self.assertEqual(find_generation(1970), "Generation X")
        
    def test_millennials(self):
        """Millennials year"""
        self.assertEqual(find_generation(1990), "Millennials")
        
    def test_generation_z(self):
        """Generation Z year"""
        self.assertEqual(find_generation(2000), "Generation Z")
        
    def test_generation_alpha(self):
        """Generation Alpha year"""
        self.assertEqual(find_generation(2015), "Generation Alpha")
        
    def test_unknown_generation(self):
        """Year outside valid ranges"""
        self.assertEqual(find_generation(1900), "Unknown")
    
    # Boundary tests
    def test_start_silent_generation(self):
        """Start of Silent Generation"""
        self.assertEqual(find_generation(1901), "Silent Generation")
        
    def test_end_silent_generation(self):
        """End of Silent Generation"""
        self.assertEqual(find_generation(1945), "Silent Generation")
        
    def test_start_baby_boomers(self):
        """Start of Baby Boomers"""
        self.assertEqual(find_generation(1946), "Baby Boomers")
        
    def test_end_baby_boomers(self):
        """End of Baby Boomers"""
        self.assertEqual(find_generation(1964), "Baby Boomers")
        
    def test_start_generation_x(self):
        """Start of Generation X"""
        self.assertEqual(find_generation(1965), "Generation X")
        
    def test_end_generation_x(self):
        """End of Generation X"""
        self.assertEqual(find_generation(1979), "Generation X")
        
    def test_start_millennials(self):
        """Start of Millennials"""
        self.assertEqual(find_generation(1980), "Millennials")
        
    def test_end_millennials(self):
        """End of Millennials"""
        self.assertEqual(find_generation(1994), "Millennials")
        
    def test_start_generation_z(self):
        """Start of Generation Z"""
        self.assertEqual(find_generation(1995), "Generation Z")
        
    def test_end_generation_z(self):
        """End of Generation Z"""
        self.assertEqual(find_generation(2009), "Generation Z")
        
    def test_start_generation_alpha(self):
        """Start of Generation Alpha"""
        self.assertEqual(find_generation(2010), "Generation Alpha")
        
    def test_end_generation_alpha(self):
        """End of Generation Alpha"""
        self.assertEqual(find_generation(2024), "Generation Alpha")