import unittest
from menu import Menu
import io
import sys

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        x = "Hello"
        
        self.assertEqual(x.casefold(), "hello", "Should be 2")

    def test_view_menu(self):
        self.menu = Menu()
        # self.assertEqual(self.menu.view(), "Tonight's Menu: Pizza, £9")
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        self.menu.view()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        print ('Output', capturedOutput.getvalue()) 
    

if __name__ == '__main__':
    unittest.main()