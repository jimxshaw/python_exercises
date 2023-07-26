import unittest
from capitalize import capitalize_title, capitalize_manual

class TestCapitalize(unittest.TestCase):
  def test_capitalize_title(self):
    word = "should we return the library book?"
    expected = "Should We Return The Library Book?"
    actual = capitalize_title(word)
    self.assertEqual(expected, actual)

  def test_capitalize_manual(self):
    word = "should we return the library book?"
    expected = "Should We Return The Library Book?"
    actual = capitalize_manual(word)
    self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
