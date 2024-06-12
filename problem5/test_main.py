import unittest
from main import max_sequence

class TestMaxSequence(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_case_2(self):
        self.assertEqual(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]), 7)

    def test_case_3(self):
        self.assertEqual(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]), 7)

    def test_case_4(self):
        self.assertEqual(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]), 8)

    def test_case_5(self):
        self.assertEqual(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]), 12)

if __name__ == "__main__":
    unittest.main()