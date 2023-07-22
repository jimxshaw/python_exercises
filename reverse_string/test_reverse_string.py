import unittest
from reverse_string import reverse_string_reversed, reverse_string_slice, reverse_string_loop, reverse_string_reduce

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        # One word.
        input = "Johnny"
        actual = reverse_string_reversed(input)
        expected = "ynnhoJ"      
        self.assertEqual(actual, expected)

        # Multiple words.
        input = "Hello World!"
        actual = reverse_string_reversed(input)        
        expected = "!dlroW olleH"
        self.assertEqual(actual, expected)

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

    def test_reverse_string_reduce(self):
        # One word.
        input = "Johnny"
        actual = reverse_string_reduce(input)
        expected = "ynnhoJ"
        self.assertEqual(actual, expected)

        # Multiple words.
        input = "Hello World!"
        actual = reverse_string_reduce(input)        
        expected = "!dlroW olleH"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
