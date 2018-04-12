"""Test foundations Module using unittest

"""

import unittest
import foundations
import pytest

class TestMinimumClasses(unittest.TestCase):

    def setUp(self):
        self.emp = foundations.Employee('Gerard', 10e3, 'VP')

    def test_employee_init(self):
        self.assertEqual(self.emp.name, 'Gerard')
        self.assertEqual( self.emp.salary, 10000)
        self.assertEqual( self.emp.rank, 'VP')

    def test_emp_give_raise(self):
        self.assertEqual( self.emp.salary, 10000)
        self.emp.give_raise(20)
        self.assertEqual( self.emp.salary, 12000)

    def tearDown(self):
        self.emp = None

class TestCollatz(unittest.TestCase):

    def test_division_by_2(self):
        self.assertEqual(foundations.collatz(10), 5)

    @unittest.skip('demo skipping')
    def test_multiply_by_3(self):
        self.assertEqual(foundations.collatz(11), 34)

    def test_hello(self):
        with self.assertRaises(TypeError):
            foundations.collatz('hello')

if __name__ == '__main__':
    unittest.main(['test_foundations_with_unittest.py'])