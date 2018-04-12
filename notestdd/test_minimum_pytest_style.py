''' To run this test, use:

        $ py.test -q test_minimum_pytest_style.py
        .
        1 passed in 0.00 seconds
'''

import pytest
import the_minimum

def test_collatz():
    assert the_minimum.collatz(10) == 5
    assert the_minimum.collatz(11) == 34

def test_collatz_bad_args():
    with pytest.raises(TypeError):
        the_minimum.collatz('hello')
