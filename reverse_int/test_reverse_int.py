import unittest
from reverse_int import reverse_int, reverse_int_sign

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

    def test_reverse_int_sign(self):
        # Input is negative.
        input = -40
        actual = reverse_int_sign(input)
        expected = -4
        self.assertEqual(actual, expected)

        # Input is positive.
        input = 500
        actual = reverse_int_sign(input)
        expected = 5
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
