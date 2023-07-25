import unittest
from anagrams import anagrams_one, anagrams_two, anagrams_sort

class TestAnagrams(unittest.TestCase):
  def test_anagram_one(self):
    expected = True
    actual = anagrams_one('RAIL! SAFETY!', 'fairy tales')
    self.assertTrue(expected, actual)

    expected = False
    actual = anagrams_one('Hi there', 'Bye there')
    self.assertFalse(expected, actual)

  def test_anagram_two(self):
    expected = True
    actual = anagrams_two('RAIL! SAFETY!', 'fairy tales')
    self.assertTrue(expected, actual)

    expected = False
    actual = anagrams_two('Hi there', 'Bye there')
    self.assertFalse(expected, actual)

  def test_anagram_sort(self):
    expected = True
    actual = anagrams_sort('RAIL! SAFETY!', 'fairy tales')
    self.assertTrue(expected, actual)

    expected = False
    actual = anagrams_sort('Hi there', 'Bye there')
    self.assertFalse(expected, actual)

if __name__ == "__main__":
    unittest.main()
