"""Test foundations Module using Beck Test Framework

"""

import unittest
import foundations

class TestMinimumClasses(unittest.TestCase):

    def setUp(self):
        self.emp = foundations.Employee('Gerard', 10e3, 'VP')

    def test_employee_init(self):
        self.emp.name == 'Gerard'
        assert self.emp.salary == 10000
        assert self.emp.rank == 'VP'

    def test_emp_give_raise(self):
        assert self.emp.salary == 10000
        self.emp.give_raise(20)
        assert self.emp.salary == 12000

    def teardown(self):
        assert self.x in [20, 100]
        del self.x

if __name__ == '__main__':
    print(beck.run_tests(TestMinimumClasses)[0])