import unittest
from fizz_buzz import fizz_buzz_while, fizz_buzz_range

class TestFizzBuzz(unittest.TestCase):
  def test_fizz_buzz_while(self):
    expected = [
      '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17', 'fizz', '19', 'buzz'
    ]

    actual = fizz_buzz_while(20)
    self.assertEqual(actual, expected)

  def test_fizz_buzz_range(self):
    expected = [
      '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17', 'fizz', '19', 'buzz'
    ]

    actual = fizz_buzz_range(20)
    self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
