import unittest
from max_char import max_char

class TestMaxChar(unittest.TestCase):
  def test_max_char(self):
    # Scenario 1
    input = 'abcccccccd'
    actual = max_char(input)
    expected = 'c'
    self.assertEqual(actual, expected)

    # Scenario 2
    input = 'apple 1231111'
    actual = max_char(input)
    expected = '1'
    self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
