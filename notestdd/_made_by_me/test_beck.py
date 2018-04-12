#######################################################
# Make sure TestResult works

from beck import TestResult

result = TestResult()

assert result.run_count == 0
assert result.failure_count == 0
assert result.summary() == '0 run, 0 failed'

result.test_started()
assert result.run_count == 1
assert  result.failure_count == 0

result.test_failed()
assert result.run_count == 1
assert result.failure_count == 1

result.test_started()
assert result.summary() == '2 run, 1 failed'

########################################################
# Make sure Raises() works

from beck import Raises

with Raises(TypeError):
    3 + 'hello'

try:
    with Raises(TypeError):
        3 + 4
except AssertionError:
    pass
except Exception:
    assert False, 'expected AssertionError'
else:
    assert False, 'expected an error'

########################################################
# Our math product

def add(x, y):
    return x * y # <== This is a bug!

def sub(x, y):
    return x - y # <== This code is correct!

#########################################################
# Testing the math functions

from beck import TestCase

class TestMathProduct(TestCase):
    def test_add(self):
        assert add(3, 5) == 8

    def test_sub(self):
        assert sub(8, 5) == 3

    def test_sub_with_bad_arguments(self):
        with self.assert_raises(TypeError):
            sub(8, 'hello')

    def test_throw_exception(self):
        raise ZeroDivisionError

#########################################################
# Test the TestCase itself

result = TestResult()
test1 = TestMathProduct('test_add', result)
assert result.summary() == '0 run, 0 failed'
test1.run()
assert result.summary() == '1 run, 1 failed'

test2 = TestMathProduct('test_sub', result)
test2.run()
assert result.summary() == '2 run, 1 failed'

test3 = TestMathProduct('test_sub_with_bad_arguments', result)
test3.run()
assert result.summary() == '3 run, 1 failed'

test4 = TestMathProduct('test_throw_exception', result)
test4.run()
assert result.summary() == '4 run, 2 failed'

########################################################
# Test the TestSuite itself

from beck import TestSuite

suite = TestSuite()
suite.add(TestMathProduct, 'test_add')
suite.add(TestMathProduct, 'test_sub')
suite.add(TestMathProduct, 'test_sub_with_bad_arguments')

result = TestResult()
suite.run(result)
assert result.summary() == '3 run, 1 failed'

########################################################
# Exercise a test runner

from beck import run_tests

summary, delta = run_tests(TestMathProduct)
assert summary == '4 run, 2 failed'
assert delta >= 0

########################################################
# Test setup() and teardown()

class VerifySetupAndTeardown(TestCase):

    def setup(self):
        self.x = 10

    def test_double(self):
        assert self.x == 10
        self.x *= 2
        assert self.x == 20

    def test_square(self):
        assert self.x == 10
        self.x **= 2
        assert self.x == 100

    def teardown(self):
        assert self.x in [20, 100]
        del self.x

assert run_tests(VerifySetupAndTeardown)[0] == '2 run, 0 failed'