"""A unittest-like framework to practice Test Driven Development.

Developed in combination with test_beck.py to practice TDD

"""

import logging as log

class TestResult:
    'Accumulate number of tests run and number of failures'
    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def summary(self):
        return '%d run, %d failed' % (self.run_count, self.failure_count)

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

class Raises:
    'Assert that a particular exception is raised.'

    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_inst, exc_tb):
        if exc_type == self.expected_exception:
            return True
        assert False, 'expected %s' % self.expected_exception

class TestCase:
    'Run a single test method and update a TestResult object.'
    def __init__(self, method_name, result):
        self.method_name = method_name
        self.result = result
    def run(self):
        class_name = type(self).__name__

        if hasattr(self, 'setup'):
            self.setup()

        test_method = getattr(self, self.method_name)
        self.result.test_started()
        try:
            test_method()
        except AssertionError:
            self.result.test_failed()
            log.info('Test %s. %s failed', class_name, self.method_name)
        except Exception:
            self.result.test_failed()
            log.exception('Test %s. %s errored', class_name, self.method_name)

        if hasattr(self, 'teardown'):
            self.teardown()

    def assert_raises(self, expected_exception):
        return Raises(expected_exception)

class TestSuite:
    'Collection of test cases to be run together.'

    def __init__(self):
        self.testcases = []

    def add(self, test_case_class, method_name):
        self.testcases.append((test_case_class, method_name))

    def run(self, result):
        for test_case_class, method_name in self.testcases:
            test_case = test_case_class(method_name, result)
            test_case.run()

import time
def run_tests(test_class):
    'Test runner with automatic discovery of test_method names.'

    suite = TestSuite()
    for method_name in dir(test_class):
        if method_name.startswith('test_'):
            suite.add(test_class, method_name)
    result = TestResult()
    start = time.time()
    suite.run(result)
    end = time.time()
    return result.summary(), (end-start)