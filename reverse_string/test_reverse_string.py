import unittest
import sys
from io import StringIO
from reverse_string import reverse_string_slice, reverse_string_loop

class TestReverseString(unittest.TestCase):
    def test_reverse_string_slice(self):
        # One word.
        input = "Johnny"
        actual = reverse_string_slice(input)
        expected = "ynnhoJ"      
        self.assertEqual(actual, expected)

        # Multiple words.
        input = "Hello World!"
        actual = reverse_string_slice(input)        
        expected = "!dlroW olleH"
        self.assertEqual(actual, expected)

    def test_reverse_string_loop(self):
        # One word.
        input = "Johnny"
        actual = reverse_string_loop(input)
        expected = "ynnhoJ"
        self.assertEqual(actual, expected)

        # Multiple words.
        input = "Hello World!"
        actual = reverse_string_loop(input)        
        expected = "!dlroW olleH"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
