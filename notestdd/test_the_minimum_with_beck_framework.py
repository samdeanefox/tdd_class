import beck
import the_minimum

import logging

logging.basicConfig(
    level=logging.INFO,
    filename='the_min_tests.log',
)

class TestMinimumClasses(beck.TestCase):

    def set_up(self):
        self.ee = the_minimum.Employee('Navra Ananda', 'female', 200)
        logging.debug('Setup Navra as an example Employee')

    def test_employee(self):
        navra = self.ee
        assert navra.name == 'Navra Ananda'
        assert navra.gender == 'female'
        assert navra.salary == 200
        navra.give_raise(10)
        assert navra.salary == 220

    def test_employee_neg_raise(self):
        navra = self.ee
        assert navra.salary == 200
        navra.give_raise(-10)
        assert navra.salary == 185      # Intentionally failing test

    def tear_down(self):
        self.ee = None

if __name__ == '__main__':
    beck.run_tests(TestMinimumClasses)
