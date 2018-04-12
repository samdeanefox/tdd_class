''' Goals:

* Develop a test framework like XUnit, JUnit, unittest, nose, py.test
* Use a test-first TDD style
* Use our framework to test itself
* Practice Python fundamentals

'''

import logging

class TestResult:
    'Accumulate number of tests run and number of failures'

    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

    def summary(self):
        return f'{self.run_count} run, {self.failure_count} failed'

class Raises:
    'Assert that a specific exception is raised'

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        if exctype == self.exception:
            return True
        assert False, f'Expected {self.exception}'

class TestCase:
    'Run a single test method'

    def __init__(self, method_name, result):
        self.method_name = method_name
        self.result = result

    def run(self):
        # Run the "set_up" method if it exists
        setup_method = getattr(self, 'set_up', None)
        if setup_method is not None:
            setup_method()

        # Record a test started. Run the test. Catch and record failures.
        self.result.test_started()
        test_method = getattr(self, self.method_name)
        try:
            test_method()
        except AssertionError:
            self.result.test_failed()
            logging.exception('Test failed: %s', self.method_name)
        else:
            logging.info('Test succeeded: %s', self.method_name)

        # Run the "tear_down" method if it exists
        teardown_method = getattr(self, 'tear_down', None)
        if teardown_method is not None:
            teardown_method()

    def assert_raises(self, exception):
        return Raises(exception)

class TestSuite:
    'A collection of test cases than can be run together'

    def __init__(self):
        self.cases = []

    def add(self, test_case_class, method_name):
        self.cases.append( (test_case_class, method_name) )

    def run(self, result):
        for test_case_class, method_name in self.cases:
            testcase = test_case_class(method_name, result)
            testcase.run()
            print('.', end='')
        print()

    def __len__(self):
        return len(self.cases)

    def __getitem__(self, index):
        return self.cases[index][1]

    def __repr__(self):
        return f'TestSuite{tuple(self)}'

def run_tests(test_class):
    'Test runner with automatic discovery of test_ method names'
    suite = TestSuite()
    for method_name in dir(test_class):
        if method_name.startswith('test_'):
            suite.add(test_class, method_name)

    result = TestResult()
    suite.run(result)
    print(result.summary())
