''' Automatic generation of simplified failing test cases.

https://hypothesis.readthedocs.io/en/latest/

'''

from hypothesis import given, assume, strategies as st
from buggy_math_module import quadratic
import cmath

@given(a=st.floats(min_value=-1000, max_value=1000), b=st.floats(), c=st.floats())
def test_quad(a, b, c):
    assume(abs(a) >= 0.1)
    assume(abs(c) >= 0.1)
    x1, x2 = quadratic(a, b, c)
    assert a*x1**2 + b*x1 + c == 0.0
    assert a*x1**2 + b*x1 + c == 0.0

if __name__ == '__main__':

    test_quad()
