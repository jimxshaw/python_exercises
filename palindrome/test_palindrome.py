import unittest
from palindrome import palindrome_slice, palindrome_reversed, palindrome_loop

class TestPalindrome(unittest.TestCase):
    def test_palindrome_slice(self):
        # Input is not palidrome.
        input = 'car'
        actual = palindrome_slice(input)
        expected = False
        self.assertEqual(actual, expected)

        # Input is palindrome.
        input = 'abba'
        actual = palindrome_slice(input)
        expected = True
        self.assertEqual(actual, expected)

    def test_palindrome_reversed(self):
        # Input is not palidrome.
        input = 'car'
        actual = palindrome_reversed(input)
        expected = False
        self.assertEqual(actual, expected)

        # Input is palindrome.
        input = 'abba'
        actual = palindrome_reversed(input)
        expected = True
        self.assertEqual(actual, expected)

    def test_palindrome_loop(self):
        # Input is not palidrome.
        input = 'car'
        actual = palindrome_loop(input)
        expected = False
        self.assertEqual(actual, expected)

        # Input is palindrome.
        input = 'abba'
        actual = palindrome_loop(input)
        expected = True
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()
