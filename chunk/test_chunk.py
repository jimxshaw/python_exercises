import unittest
from chunk import chunk, chunk_manual

class TestChunk(unittest.TestCase):
  def test_chunk(self):
    arr = [1, 2, 3, 4, 5]
    expected = [[1, 2], [3, 4], [5]]
    actual = chunk(arr, 2)
    self.assertEqual(expected, actual)

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = [[ 1, 2, 3], [4, 5, 6], [7, 8]]
    actual = chunk(arr, 3)
    self.assertEqual(expected, actual)

    arr = [1, 2, 3]
    expected = [[1], [2], [3]]
    actual = chunk(arr, 1)
    self.assertEqual(expected, actual)

  def test_chunk_manual(self):
    arr = [1, 2, 3, 4, 5]
    expected = [[1, 2], [3, 4], [5]]
    actual = chunk_manual(arr, 2)
    self.assertEqual(expected, actual)

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = [[ 1, 2, 3], [4, 5, 6], [7, 8]]
    actual = chunk_manual(arr, 3)
    self.assertEqual(expected, actual)

    arr = [1, 2, 3]
    expected = [[1], [2], [3]]
    actual = chunk_manual(arr, 1)
    self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()