import unittest
from reverse_int import reverse_int

class TestReverseInt(unittest.TestCase):
    def test_reverse_int(self):
        # Input is negative.
        input = -123
        actual = reverse_int(input)
        expected = -321
        self.assertEqual(actual, expected)

        # Input is positive.
        input = 500
        actual = reverse_int(input)
        expected = 5
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
