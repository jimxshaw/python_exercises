import unittest
from pyramid import pyramid

class TestPyramid(unittest.TestCase):

    def test_pyramid(self):
        self.assertEqual(pyramid(1), '#')
        self.assertEqual(pyramid(2), ' # \n###')
        self.assertEqual(pyramid(3), '  #  \n ### \n#####')
        self.assertEqual(pyramid(4), '   #   \n  ###  \n ##### \n#######')

if __name__ == "__main__":
    unittest.main()
