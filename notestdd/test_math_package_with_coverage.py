''' How to measure test coverage.
    https://coverage.readthedocs.io/en/coverage-4.4.1/cmd.html

    Command-line API:
        coverage run test_math_package.py
        coverage report
        coverage annotate
        coverage html

'''

import unittest
import buggy_math_module

class TestMathStuff(unittest.TestCase):

    def test_quadratic(self):
        a = 8
        b = -14
        c = -15
        x1, x2 = buggy_math_module.quadratic(a, b, c)
        self.assertEqual(a*x1**2 + b*x1 + c, 0)
        self.assertEqual(a*x2**2 + b*x2 + c, 0)

        # This gives 100% coverage but misses the
        # case with a negative discrimant!

if __name__ == '__main__':

    unittest.main()
