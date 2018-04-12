"""Test foundations Module using pytest

"""

import unittest
import foundations
import pytest

def emp():
    return foundations.Employee('Gerard', 10e3)

def test_employee_init(emp):
    assert emp.name == 'Gerard'
    assert emp.salary == 10000
    assert emp.rank == 'VP'

def test_emp_give_raise(emp):
    assert emp.salary == 10000
    emp.give_raise(20)
    assert emp.salary == 12000


def test_division_by_2():
    assert foundations.collatz(10) == 5

@unittest.skip('demo skipping')
def test_multiply_by_3():
    assert foundations.collatz(11) == 34

def test_hello():
    with pytest.raises(TypeError):
            foundations.collatz('hello')