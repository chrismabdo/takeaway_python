import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        x = "Hello"
        
        self.assertEqual(x.casefold(), "hello", "Should be 2")

if __name__ == '__main__':
    unittest.main()