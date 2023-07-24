import unittest
from happy_number import is_number_happy

class TestHappyNumber(unittest.TestCase):
  def test_happy_number_19(self):
        self.assertTrue(is_number_happy(19))

  def test_non_happy_number_20(self):
      self.assertFalse(is_number_happy(20))

  def test_happy_number_7(self):
      self.assertTrue(is_number_happy(7))

  def test_non_happy_number_16(self):
      self.assertFalse(is_number_happy(16))

  def test_happy_number_139(self):
      self.assertTrue(is_number_happy(139))

  def test_non_happy_number_145(self):
      self.assertFalse(is_number_happy(145))

if __name__ == '__main__':
    unittest.main()