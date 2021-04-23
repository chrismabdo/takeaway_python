import unittest
from menu import Menu

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        x = "Hello"
        
        self.assertEqual(x.casefold(), "hello", "Should be 2")

    def test_view_menu(self):
        menu = Menu()
        self.assertEqual(menu.view(), print("Tonight's Menu: Pizza, £9"))

if __name__ == '__main__':
    unittest.main()