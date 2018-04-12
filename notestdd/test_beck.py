from beck import TestResult, TestCase, TestSuite, run_tests

##########################################################
# These are the tests for our product

def add(x, y):
    return x * y            # <== Intentionally buggy code

def sub(x, y):
    return x - y            # <== Intentionally correct code

class TestMathFunctions(TestCase):

    def test_add(self):
        assert add(3, 5) == 8

    def test_sub(self):
        assert sub(10, 3) == 7

    def test_sub_bad_args(self):
        with self.assert_raises(TypeError):
            sub(70, 'hello')

# Tests for the Test Result Class #######################

result = TestResult()

assert result.run_count == 0
assert result.summary() == '0 run, 0 failed'
result.test_started()
assert result.run_count == 1
assert result.summary() == '1 run, 0 failed'

assert result.failure_count == 0
result.test_failed()
assert result.failure_count == 1
assert result.summary() == '1 run, 1 failed'

#########################################################

result = TestResult()

test = TestMathFunctions('test_add', result)
assert result.summary() == '0 run, 0 failed'
test.run()
assert result.summary() == '1 run, 1 failed'

test = TestMathFunctions('test_sub', result)
test.run()
assert result.summary() == '2 run, 1 failed'

print('Done!')

#########################################################

suite = TestSuite()
suite.add(TestMathFunctions, 'test_add')
suite.add(TestMathFunctions, 'test_sub')
suite.add(TestMathFunctions, 'test_sub_bad_args')

result = TestResult()
suite.run(result)
print(result.summary())
assert len(suite) == 3
assert suite[1] == 'test_sub'
assert repr(suite) == "TestSuite('test_add', 'test_sub', 'test_sub_bad_args')"

#########################################################



