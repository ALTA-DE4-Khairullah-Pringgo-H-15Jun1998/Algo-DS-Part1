import unittest
from main import primeX

class TestPrimeX(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(primeX(1), 2)

    def test_case_5(self):
        self.assertEqual(primeX(5), 11)

    def test_case_8(self):
        self.assertEqual(primeX(8), 19)

    def test_case_9(self):
        self.assertEqual(primeX(9), 23)

    def test_case_10(self):
        self.assertEqual(primeX(10), 29)

if __name__ == "__main__":
    unittest.main()