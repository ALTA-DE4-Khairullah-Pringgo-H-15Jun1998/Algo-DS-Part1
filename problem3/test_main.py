import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_case_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_case_9(self):
        self.assertEqual(fibonacci(9), 34)

    def test_case_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_case_12(self):
        self.assertEqual(fibonacci(12), 144)

if __name__ == "__main__":
    unittest.main()