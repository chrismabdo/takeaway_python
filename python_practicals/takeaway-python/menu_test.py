import unittest
from menu import Menu
from basket import Basket
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
    
    def test_for_cart(self):
        self.basket = Basket()
        self.assertEqual(self.basket.cart, [], "Should be an empty array")

    def test_for_adding_item_to_cart(self):
        self.basket = Basket()
        self.basket.add_item("Ice-Cream", 2)
        self.assertEqual(self.basket.cart, ["Ice-Cream", "Ice-Cream"], "Shoud have added two ice-creams to cart")

    def test_for_adding_incorrect_item_to_cart(self):
        self.basket = Basket()
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput 
        self.basket.add_item("Sushi", 2) 
        sys.stdout = sys.__stdout__                     # Reset redirect.
        print ('Output', capturedOutput.getvalue())

    def test_total_price(self):
        self.basket = Basket()
        self.basket.add_item("Ice-Cream", 3)
        self.assertEqual(self.basket.check_total(), "Your Total Comes to £9", "Total Price of basket shoudl equal £9")



if __name__ == '__main__':
    unittest.main()