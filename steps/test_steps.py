import unittest
import io
import sys
from contextlib import redirect_stdout
from steps import steps, steps_recursion

class TestStepsFunction(unittest.TestCase):
    
    def test_steps(self):
        f = io.StringIO()
        with redirect_stdout(f):
            steps(2)
        s = f.getvalue()
        expected_output = "# \n##\n"
        self.assertEqual(s, expected_output)

        f = io.StringIO()
        with redirect_stdout(f):
            steps(3)
        s = f.getvalue()
        expected_output = "#  \n## \n###\n"
        self.assertEqual(s, expected_output)

        f = io.StringIO()
        with redirect_stdout(f):
            steps(4)
        s = f.getvalue()
        expected_output = "#   \n##  \n### \n####\n"
        self.assertEqual(s, expected_output)

    def test_steps_recursion(self):
        f = io.StringIO()
        with redirect_stdout(f):
            steps_recursion(2)
        s = f.getvalue()
        expected_output = "# \n##\n"
        self.assertEqual(s, expected_output)

        f = io.StringIO()
        with redirect_stdout(f):
            steps_recursion(3)
        s = f.getvalue()
        expected_output = "#  \n## \n###\n"
        self.assertEqual(s, expected_output)

        f = io.StringIO()
        with redirect_stdout(f):
            steps_recursion(4)
        s = f.getvalue()
        expected_output = "#   \n##  \n### \n####\n"
        self.assertEqual(s, expected_output)

if __name__ == '__main__':
    unittest.main()
