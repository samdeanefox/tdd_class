Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 200 * 10 // 8
250
>>> 200 * (10 // 8)
200
>>> 
=== RESTART: /Users/raymond/Dropbox/Public/sj164/how_dunder_name_works.py ===
My name is __main__
What I like to do:
Some module level docstring
>>> import how_dunder_name_works
My name is how_dunder_name_works
What I like to do:
Some module level docstring
>>> 
=== RESTART: /Users/raymond/Dropbox/Public/sj164/how_dunder_name_works.py ===
My name is __main__
What I like to do:
Some module level docstring
Woohoo! I was run directly.
>>> import how_dunder_name_works
My name is how_dunder_name_works
What I like to do:
Some module level docstring
Oh no!  I was imported
>>> print(10, 20, 30+3)
10 20 33
>>> print('hello world')
hello world
>>> print('hello', 'world')
hello world
>>> pow(2, 5)
32
>>> print('hello', 'world', sep='~')
hello~world
>>> 
=== RESTART: /Users/raymond/Dropbox/Public/sj164/how_dunder_name_works.py ===
My name is __main__
What I like to do:
Some module level docstring
Woohoo! I was run directly.
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/how_dunder_name_works.py", line 16, in <module>
    print(square(5))
TypeError: square() takes 0 positional arguments but 1 was given
>>> 
=== RESTART: /Users/raymond/Dropbox/Public/sj164/how_dunder_name_works.py ===
My name is __main__
What I like to do:
Some module level docstring
Woohoo! I was run directly.
25
>>> 
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46
male
male
>>> 
>>> 
>>> 
>>> vikas
<__main__.Employee object at 0x1034d3278>
>>> type(vikas)
<class '__main__.Employee'>
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male', 'salary': 35}
>>> 
>>> 
>>> vikas.gender
'male'
>>> vikas.company
'Cisco'
>>> 
>>> 
>>> v = 'gender'
>>> vikas.v
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    vikas.v
AttributeError: 'Employee' object has no attribute 'v'
>>> 
>>> 
>>> getattr(vikas, v)
'male'
>>> 
>>> 
>>> vikas.give_raise(30)
>>> 
>>> v = 'give_raise'
>>> getattr(vikas, v)(30)
>>> vars(v)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    vars(v)
TypeError: vars() argument must have __dict__ attribute
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male', 'salary': 58}
>>> getattr(vikas, 'get_raise')(30)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    getattr(vikas, 'get_raise')(30)
AttributeError: 'Employee' object has no attribute 'get_raise'
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46
male
male
>>> vikas.salary
35
>>> vikas.age
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    vikas.age
AttributeError: 'Employee' object has no attribute 'age'
>>> 
>>> 
>>> getattr(vikas, 'salary', 0)
35
>>> getattr(vikas, 'age', -1)
-1
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> x = 10
>>> print(f'The value of x is {x}')
The value of x is 10
>>> print(f'The value of x is {x}'.format(x=x))
The value of x is 10
>>> print(f'The value of x is {x}')
The value of x is 10
>>> dir()
['FrameworkTest', 'FrameworkTestNoSetupNoTeardown', 'TestCase', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'test', 'x']
>>> from pprint import pprint
>>> pprint(dir())
['FrameworkTest',
 'FrameworkTestNoSetupNoTeardown',
 'TestCase',
 '__annotations__',
 '__builtins__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'pprint',
 'test',
 'x']
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 25, in <module>
    result = TestResult()
NameError: name 'TestResult' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 28, in <module>
    assert result.run_count == 0
AttributeError: 'TestResult' object has no attribute 'run_count'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 31, in <module>
    result.print_summary()
AttributeError: 'TestResult' object has no attribute 'print_summary'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 35, in <module>
    result.test_started()
AttributeError: 'TestResult' object has no attribute 'test_started'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 35, in <module>
    result.test_started()
AttributeError: 'TestResult' object has no attribute 'test_started'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 35, in <module>
    result.test_started()
AttributeError: 'TestResult' object has no attribute 'test_started'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 35, in <module>
    result.test_started()
AttributeError: 'TestResult' object has no attribute 'test_started'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 39, in <module>
    assert result.run_count == 1
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Done!
>>> 
>>> x = 10                   # The variable "x" is set to 10.  There is no output
>>> x
10
>>> x == 10                  # This tests whether "x" is equal to 10.  The output is True or False
True
>>> 
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 42, in <module>
    assert result.failure_count == 0
AttributeError: 'TestResult' object has no attribute 'failure_count'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 44, in <module>
    result.test_failed()
AttributeError: 'TestResult' object has no attribute 'test_failed'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 48, in <module>
    assert result.failure_count == 1
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 47, in <module>
    result.test_failed()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 31, in test_failed
    selfl.failure_count += 1
NameError: name 'selfl' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 49, in <module>
    assert result.summary() == '1 run, 1 failed'
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Done!
>>> 
>>> 
>>> def square(x):
	x ** 2

	
>>> square(5)
>>> def square(x):
	return x ** 2

>>> square(5)
25
>>> def square(x):
	return f'The square of x is {x ** 2}'

>>> square(5)
'The square of x is 25'
>>> 
>>> 
>>> 
>>> s = [10, 20, 30]
>>> s[0]
10
>>> s[2]
30
>>> s[50]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s[50]
IndexError: list index out of range
>>> 
>>> try:
	print(s[50])
except IndexError:
	print('Oops, I did it again.')

	
Oops, I did it again.
>>> try:
	print(s[50])
except IndexError:
	print('Oops, I did it again.')
else:
	print('Woohoo! I worked')

	
Oops, I did it again.
>>> try:
	print(s[1])
except IndexError:
	print('Oops, I did it again.')
else:
	print('Woohoo! I worked')

	
20
Woohoo! I worked
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 105, in <module>
    test.test_running()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 56, in test_running
    self.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 49, in run
    method()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 69, in some_method
    assert 3 + 5 == 150
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 109, in <module>
    test.test_running()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 56, in test_running
    self.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 49, in run
    method()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 73, in test_add
    assert add(3, 5) == 8
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 106, in <module>
    test = FrameworkTest('test_add', result)
TypeError: __init__() takes 2 positional arguments but 3 were given
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 111, in <module>
    test.test_running()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 57, in test_running
    self.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 50, in run
    method()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 73, in test_add
    assert add(3, 5) == 8
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 115, in <module>
    assert result.summary() == '1 run, 1 failed'
AssertionError
>>> result.summary()
'0 run, 0 failed'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 115, in <module>
    assert result.summary() == '1 run, 1 failed'
AssertionError
>>> result.summary()
'0 run, 1 failed'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 137, in <module>
    test = FrameworkTest('test_sub')
TypeError: __init__() missing 1 required positional argument: 'result'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
0 run, 0 failed
1 run, 0 failed
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 111, in <module>
    suite = TestSuite()
NameError: name 'TestSuite' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 118, in <module>
    suite.add(TestMathFunctions, 'test_add')
AttributeError: 'TestSuite' object has no attribute 'add'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 125, in <module>
    suite.run(result)
AttributeError: 'TestSuite' object has no attribute 'run'
>>> vars(suite)
{'test_case_class': <class '__main__.TestMathFunctions'>, 'method_name': 'test_sub'}
>>> 
>>> s = [10, 20, 30]
>>> s.append(40)
>>> s
[10, 20, 30, 40]
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 127, in <module>
    suite.run(result)
AttributeError: 'TestSuite' object has no attribute 'run'
>>> vars(suite)
{'cases': [(<class '__main__.TestMathFunctions'>, 'test_add'), (<class '__main__.TestMathFunctions'>, 'test_sub')]}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 130, in <module>
    suite.run(result)
TypeError: run() takes 1 positional argument but 2 were given
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
<bound method TestResult.summary of <__main__.TestResult object at 0x1034bcef0>>
>>> result.summary
<bound method TestResult.summary of <__main__.TestResult object at 0x1034bcef0>>
>>> result.summary()
'0 run, 0 failed'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 160, in <module>
    t_suite.add(TestMinimumClasses, 'test_employee')
NameError: name 't_suite' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
1 run, 0 failed
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
2 run, 0 failed
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
2 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 173, in <module>
    run_tests(TestMinimumClasses, ['test_employee',
NameError: name 'run_tests' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
2 run, 0 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 176, in <module>
    'test_employee_neg_raise'])
TypeError: run_tests() takes 0 positional arguments but 2 were given
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
2 run, 0 failed
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
2 run, 0 failed
test_employee
test_employee_neg_raise
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
2 run, 1 failed
2 run, 0 failed
2 run, 0 failed
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.062s

OK
>>> x = 20; print(x**2)
400
>>> x = 20; print(x**2); print(x**3)
400
8000
>>> x = 20; print(x**2, end=''); print(x**3)
4008000
>>> x = 20; print(x**2, end=' '); print(x**3)
400 8000
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
..
2 run, 1 failed
..
2 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
Done!
..
2 run, 1 failed
..
2 run, 0 failed
Done!
..
2 run, 1 failed
..
2 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
Done!
..
2 run, 1 failed
..
2 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
Done!
..
2 run, 1 failed
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.058s

OK
>>> 
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
>>> cos(3.0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    cos(3.0)
NameError: name 'cos' is not defined
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(math)
Help on module math:

NAME
    math

MODULE REFERENCE
    https://docs.python.org/3.6/library/math
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the inverse hyperbolic cosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the inverse hyperbolic sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the inverse hyperbolic tangent of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return a float with the magnitude (absolute value) of x but the sign 
        of y. On platforms that support signed zeros, copysign(1.0, -0.0) 
        returns -1.0.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    gcd(...)
        gcd(x, y) -> int
        greatest common divisor of x and y
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool
        
        Determine whether two floating point numbers are close in value.
        
           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    log2(...)
        log2(x)
        
        Return the base 2 logarithm of x.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload/math.cpython-36m-darwin.so


>>> help(math.cos)
Help on built-in function cos in module math:

cos(...)
    cos(x)
    
    Return the cosine of x (measured in radians).

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'log', 'math', 'tan']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
>>> import pprint
>>> pprint.pprint(dir(math))
['__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'acos',
 'acosh',
 'asin',
 'asinh',
 'atan',
 'atan2',
 'atanh',
 'ceil',
 'copysign',
 'cos',
 'cosh',
 'degrees',
 'e',
 'erf',
 'erfc',
 'exp',
 'expm1',
 'fabs',
 'factorial',
 'floor',
 'fmod',
 'frexp',
 'fsum',
 'gamma',
 'gcd',
 'hypot',
 'inf',
 'isclose',
 'isfinite',
 'isinf',
 'isnan',
 'ldexp',
 'lgamma',
 'log',
 'log10',
 'log1p',
 'log2',
 'modf',
 'nan',
 'pi',
 'pow',
 'radians',
 'sin',
 'sinh',
 'sqrt',
 'tan',
 'tanh',
 'tau',
 'trunc']
>>> # pprint.pprint in new york, new york
>>> # cous cous and mahi mahi with Boutrous Boutrous Gali
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'log', 'math', 'square', 'tan']
>>> help(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> square(11)
121
>>> square.__name__
'square'
>>> square.__class__
<class 'function'>
>>> square.__doc__
'Return a value times itself'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
>>> square(111)
12321
>>> square(1111)
1234321
>>> square(11111)
123454321
>>> square(111111)
12345654321
>>> square(1111111)
1234567654321
>>> square(11111111)
123456787654321
>>> square(111111111)
12345678987654321
>>> square(1111111111)
1234567900987654321
>>> 0x35
53
>>> 
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list(map(square, range(10, 20)))
[100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> list(map(square, [2, 4, 6, 8]))
[4, 16, 36, 64]
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> # lambda <-- make function
>>> lambda x: x**2
<function <lambda> at 0x1046c27b8>
>>> (lambda x: x**2)(11)
121
>>> lambda x: 3*x + 1
<function <lambda> at 0x1046c27b8>
>>> (lambda x: 3*x + 1)(10)
31
>>> 100 + (lambda x: 3*x + 1)(10) + 200
331
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> f = lambda x: x**3
>>> f.__class__
<class 'function'>
>>> f.__name__
'<lambda>'
>>> f.__doc__ is None
True
>>> f.__name__ = 'big_f'
>>> f.__name__
'big_f'
>>> f.__doc__ = 'three dimensional square'
>>> f.__doc__
'three dimensional square'
>>> 
>>> help(f)
Help on function big_f in module __main__:

big_f(x)
    three dimensional square

>>> __doc__
' Fast tour of the Python world.\n    No time for details :-)\n'
>>> square.__doc__
'Return a value times itself'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> type(f)
<class '_io.TextIOWrapper'>
>>> isinstance(f, file)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    isinstance(f, file)
NameError: name 'file' is not defined
>>> isinstance(f, file)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    isinstance(f, file)
NameError: name 'file' is not defined



>>> 
>>> 


>>> 












>>> 
>>> type(f)
<class '_io.TextIOWrapper'>
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> help(f)
Help on TextIOWrapper object:

class TextIOWrapper(_TextIOBase)
 |  Character and line based layer over a BufferedIOBase object, buffer.
 |  
 |  encoding gives the name of the encoding that the stream will be
 |  decoded or encoded with. It defaults to locale.getpreferredencoding(False).
 |  
 |  errors determines the strictness of encoding and decoding (see
 |  help(codecs.Codec) or the documentation for codecs.register) and
 |  defaults to "strict".
 |  
 |  newline controls how line endings are handled. It can be None, '',
 |  '\n', '\r', and '\r\n'.  It works as follows:
 |  
 |  * On input, if newline is None, universal newlines mode is
 |    enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
 |    these are translated into '\n' before being returned to the
 |    caller. If it is '', universal newline mode is enabled, but line
 |    endings are returned to the caller untranslated. If it has any of
 |    the other legal values, input lines are only terminated by the given
 |    string, and the line ending is returned to the caller untranslated.
 |  
 |  * On output, if newline is None, any '\n' characters written are
 |    translated to the system default line separator, os.linesep. If
 |    newline is '' or '\n', no translation takes place. If newline is any
 |    of the other legal values, any '\n' characters written are translated
 |    to the given string.
 |  
 |  If line_buffering is True, a call to flush is implied when a call to
 |  write contains a newline character.
 |  
 |  Method resolution order:
 |      TextIOWrapper
 |      _TextIOBase
 |      _IOBase
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __getstate__(...)
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  close(self, /)
 |      Flush and close the IO object.
 |      
 |      This method has no effect if the file is already closed.
 |  
 |  detach(self, /)
 |      Separate the underlying buffer from the TextIOBase and return it.
 |      
 |      After the underlying buffer has been detached, the TextIO is in an
 |      unusable state.
 |  
 |  fileno(self, /)
 |      Returns underlying file descriptor if one exists.
 |      
 |      OSError is raised if the IO object does not use a file descriptor.
 |  
 |  flush(self, /)
 |      Flush write buffers, if applicable.
 |      
 |      This is not implemented for read-only and non-blocking streams.
 |  
 |  isatty(self, /)
 |      Return whether this is an 'interactive' stream.
 |      
 |      Return False if it can't be determined.
 |  
 |  read(self, size=-1, /)
 |      Read at most n characters from stream.
 |      
 |      Read from underlying buffer until we have n characters or we hit EOF.
 |      If n is negative or omitted, read until EOF.
 |  
 |  readable(self, /)
 |      Return whether object was opened for reading.
 |      
 |      If False, read() will raise OSError.
 |  
 |  readline(self, size=-1, /)
 |      Read until newline or EOF.
 |      
 |      Returns an empty string if EOF is hit immediately.
 |  
 |  seek(self, cookie, whence=0, /)
 |      Change stream position.
 |      
 |      Change the stream position to the given byte offset. The offset is
 |      interpreted relative to the position indicated by whence.  Values
 |      for whence are:
 |      
 |      * 0 -- start of stream (the default); offset should be zero or positive
 |      * 1 -- current stream position; offset may be negative
 |      * 2 -- end of stream; offset is usually negative
 |      
 |      Return the new absolute position.
 |  
 |  seekable(self, /)
 |      Return whether object supports random access.
 |      
 |      If False, seek(), tell() and truncate() will raise OSError.
 |      This method may need to do a test seek().
 |  
 |  tell(self, /)
 |      Return current stream position.
 |  
 |  truncate(self, pos=None, /)
 |      Truncate file to size bytes.
 |      
 |      File pointer is left unchanged.  Size defaults to the current IO
 |      position as reported by tell().  Returns the new size.
 |  
 |  writable(self, /)
 |      Return whether object was opened for writing.
 |      
 |      If False, write() will raise OSError.
 |  
 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  buffer
 |  
 |  closed
 |  
 |  encoding
 |      Encoding of the text stream.
 |      
 |      Subclasses should override.
 |  
 |  errors
 |      The error setting of the decoder or encoder.
 |      
 |      Subclasses should override.
 |  
 |  line_buffering
 |  
 |  name
 |  
 |  newlines
 |      Line endings translated so far.
 |      
 |      Only line endings translated during reading are considered.
 |      
 |      Subclasses should override.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from _IOBase:
 |  
 |  __del__(...)
 |  
 |  __enter__(...)
 |  
 |  __exit__(...)
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  readlines(self, hint=-1, /)
 |      Return a list of lines from the stream.
 |      
 |      hint can be specified to control the number of lines read: no more
 |      lines will be read if the total size (in bytes/characters) of all
 |      lines so far exceeds hint.
 |  
 |  writelines(self, lines, /)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from _IOBase:
 |  
 |  __dict__

>>> 
>>> 
>>> help(f.read)
Help on built-in function read:

read(size=-1, /) method of _io.TextIOWrapper instance
    Read at most n characters from stream.
    
    Read from underlying buffer until we have n characters or we hit EOF.
    If n is negative or omitted, read until EOF.

>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> f.closed
False
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 'write'
'write'
>>> 
>>> 
>>> 
>>> 
>>> type(f)
<class '_io.TextIOWrapper'>
>>> type(data)
<class 'str'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
>>> f.closed
False
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
>>> f.closed
True
>>> print(data)
CSCO,100,18.04
ANTM,200,45.03
CSCO,150,19.05
MSFT,250,80.56
IBM,500,22.01
ANTM,250,44.23
GOOG,200,501.45
CSCO,175,19.56
MSFT,75,80.81
GOOG,300,502.65
IBM,150,25.01

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 27, in <module>
    print( 32 / 0 )
ZeroDivisionError: division by zero
>>> f.closed
False
>>> not f.closed
True
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 28, in <module>
    print( 32 / 0 )
ZeroDivisionError: division by zero
>>> not f.closed
False
>>> f.closed
True
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
>>> f.closed
True
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 40, in <module>
    os.remove('xyzpdq.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'xyzpdq.txt'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> {'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> hash('matthew')
-1307316866709166687
>>> 
=============================== RESTART: Shell ===============================
>>> hash('matthew')
8002240970845275502
>>> {'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> {'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> {'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 63, in <module>
    print( brand['susan'] )
KeyError: 'susan'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
>>> 

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 78, in <module>
    print( brands.keys() )
NameError: name 'brands' is not defined
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
>>> animals = {'dragons': 3}
>>> animals.get('dragons', 0)
3
>>> animals.get('unicorns', 0)
0
>>> # Guido van Rossum
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'tom']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'mstthew']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
>>> dir(names)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(names)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 98, in <module>
    print( names[50] )
IndexError: list index out of range
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
>>> names
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0, 10)) + list(range(10, 20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(0, 10)) + list(range(10, 20)) == list(range(0, 20))
True
>>> s = 'the tale of two cities'
>>> s[:3]
'the'
>>> tale[4:8]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    tale[4:8]
NameError: name 'tale' is not defined
>>> s[4:8]
'tale'
>>> s[0:4] + s[4:8] == s[0:8]
True
>>> s[0:4]
'the '
>>> s[:4]
'the '
>>> s[0]
't'
>>> s[0] + s[1]
'th'
>>> s[0] + s[1] + s[2]
'the'
>>> s[0] + s[1] + s[2] + s[3]
'the '
>>> f = open('notestdd/hamlet.txt')
>>> lines = f.readlines()
>>> type(lines)
<class 'list'>
>>> len(lines)
7883
>>> for line in lines[:10]:
	print(line)

	
The Tragedy of Hamlet, Prince of Denmark

Shakespeare homepage | Hamlet | Entire play

ACT I

SCENE I. Elsinore. A platform before the castle.



    FRANCISCO at his post. Enter to him BERNARDO 



BERNARDO



    Who's there?

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
WARNING:root:Running low on disk space
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
WARNING:root:Running low on disk space
ERROR:root:Oh no, the data input file is missing
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
WARNING:root:Running low on disk space
ERROR:root:Oh no, the data input file is missing
CRITICAL:root:The CPU is melting
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO:root:The human head weight 8 and 1/2 pounds
WARNING:root:Running low on disk space
ERROR:root:Oh no, the data input file is missing
CRITICAL:root:The CPU is melting
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO:root:The human head weight 8 and 1/2 pounds
WARNING:root:Running low on disk space
ERROR:root:Oh no, the data input file is missing
CRITICAL:root:The CPU is melting
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 129, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO:root:The human head weight 8 and 1/2 pounds
WARNING:root:Running low on disk space
ERROR:root:Oh no, the data input file is missing
CRITICAL:root:The CPU is melting
ERROR:root:Tried to divide 32
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 130, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO
WARNING
ERROR
CRITICAL
ERROR
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 133, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO | 2017-07-11 15:54:47,011
WARNING | 2017-07-11 15:54:47,060
ERROR | 2017-07-11 15:54:47,111
CRITICAL | 2017-07-11 15:54:47,160
ERROR | 2017-07-11 15:54:47,211
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 133, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
    INFO | 2017-07-11 15:55:10,185
 WARNING | 2017-07-11 15:55:10,233
   ERROR | 2017-07-11 15:55:10,284
CRITICAL | 2017-07-11 15:55:10,332
   ERROR | 2017-07-11 15:55:10,384
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 133, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO     | 2017-07-11 15:55:37,922
WARNING  | 2017-07-11 15:55:37,970
ERROR    | 2017-07-11 15:55:38,022
CRITICAL | 2017-07-11 15:55:38,071
ERROR    | 2017-07-11 15:55:38,121
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 133, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
INFO     | 2017-07-11 15:55:50,328 | The human head weight 8 and 1/2 pounds
WARNING  | 2017-07-11 15:55:50,375 | Running low on disk space
ERROR    | 2017-07-11 15:55:50,427 | Oh no, the data input file is missing
CRITICAL | 2017-07-11 15:55:50,477 | The CPU is melting
ERROR    | 2017-07-11 15:55:50,526 | Tried to divide 32
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 133, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
..
2 run, 0 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
.ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 21, in test_employee_neg_raise
    assert navra.salary == 185
AssertionError
.
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
..
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
.ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 27, in test_employee_neg_raise
    assert navra.salary == 185
AssertionError
.
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
INFO:root:Test succeeded: test_employee
.ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 27, in test_employee_neg_raise
    assert navra.salary == 185
AssertionError
.
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
..
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
INFO:root:Test succeeded: test_employee
.ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 29, in test_employee_neg_raise
    assert navra.salary == 185
AssertionError
.
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
DEBUG:root:Setup Navra as an example Employee
INFO:root:Test succeeded: test_employee
.DEBUG:root:Setup Navra as an example Employee
ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 29, in test_employee_neg_raise
    assert navra.salary == 185
AssertionError
.
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
..
2 run, 1 failed
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
>>> 
>>> 
>>> type(u)
<class 'http.client.HTTPResponse'>
>>> dir(u)
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
>>> type(page)
<class 'bytes'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 145, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 146, in <module>
    print(32 / 0)
ZeroDivisionError: division by zero
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
>>> print(page[:300])
b'<?xml version="1.0" encoding="utf-8" ?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
>>> type(s)
<class 'set'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
>>> s
{10, 20, 30}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
>>> s.symmetric_difference(t)
{40, 10}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
>>> url.split('.')
['http://www', 'cisco', 'com/forums/python/games', 'html']
>>> url.split('.')[-1]
'html'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
>>> type(s)
<class 'str'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
>>> type(b1)
<class 'bytes'>
>>> type(b2)
<class 'bytes'>
>>> type(b3)
<class 'bytes'>
>>> len(b1)
92
>>> len(b2)
46
>>> len(b3)
24
>>> list(b1)
[255, 254, 0, 0, 84, 0, 0, 0, 104, 0, 0, 0, 101, 0, 0, 0, 32, 0, 0, 0, 97, 0, 0, 0, 110, 0, 0, 0, 115, 0, 0, 0, 119, 0, 0, 0, 101, 0, 0, 0, 114, 0, 0, 0, 32, 0, 0, 0, 105, 0, 0, 0, 115, 0, 0, 0, 32, 0, 0, 0, 100, 6, 0, 0, 98, 6, 0, 0, 32, 0, 0, 0, 116, 0, 0, 0, 111, 0, 0, 0, 100, 0, 0, 0, 97, 0, 0, 0, 121, 0, 0, 0]
>>> list(b2)
[255, 254, 84, 0, 104, 0, 101, 0, 32, 0, 97, 0, 110, 0, 115, 0, 119, 0, 101, 0, 114, 0, 32, 0, 105, 0, 115, 0, 32, 0, 100, 6, 98, 6, 32, 0, 116, 0, 111, 0, 100, 0, 97, 0, 121, 0]
>>> list(b3)
[84, 104, 101, 32, 97, 110, 115, 119, 101, 114, 32, 105, 115, 32, 217, 164, 217, 162, 32, 116, 111, 100, 97, 121]
>>> 
>>> list(map(ord, s))
[84, 104, 101, 32, 97, 110, 115, 119, 101, 114, 32, 105, 115, 32, 1636, 1634, 32, 116, 111, 100, 97, 121]
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
b'\xff\xfe\x00\x00T\x00\x00\x00h\x00\x00\x00e\x00\x00\x00 \x00\x00\x00a\x00\x00\x00n\x00\x00\x00s\x00\x00\x00w\x00\x00\x00e\x00\x00\x00r\x00\x00\x00 \x00\x00\x00i\x00\x00\x00s\x00\x00\x00 \x00\x00\x00d\x06\x00\x00b\x06\x00\x00 \x00\x00\x00t\x00\x00\x00o\x00\x00\x00d\x00\x00\x00a\x00\x00\x00y\x00\x00\x00'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
 T h e   a n s w e r   i s   ٤ ٢   t o d a y 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
The answer is ٤٢ today
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/basics.py", line 189, in <module>
    print(b2.decode('utf-8'))
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
>>> color
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
>>> type(dict)
<class 'type'>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
>>> type(s1)
<class 'str'>
>>> type(s2)
<class 'bytes'>
>>> type(s3)
<class 'bytes'>
>>> type(s4)
<class 'str'>
>>> s1
'{"raymond": "red", "rachel": "blue", "matthew": "yellow"}'
>>> s2
b'\x80\x03}q\x00(X\x07\x00\x00\x00raymondq\x01X\x03\x00\x00\x00redq\x02X\x06\x00\x00\x00rachelq\x03X\x04\x00\x00\x00blueq\x04X\x07\x00\x00\x00matthewq\x05X\x06\x00\x00\x00yellowq\x06u.'
>>> s3
b'\xfb\xda\x07raymond\xda\x03red\xda\x06rachel\xda\x04blue\xda\x07matthew\xda\x06yellow0'
>>> s4
'raymond=red&rachel=blue&matthew=yellow'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/basics.py ===========
-0.9899924966004454
-0.1425465430742778 1.0986122886681098
121
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
164
164
<class 'dict'>
{'raymond': 'mac', 'rachel': 'pc', 'matthew': 'vtech'}
3
pc
True
Oops, I did it again
I made you believe
we're more than just friends
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'list'>
5
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
['raymond', 'rachel', 'matthew', 'susan', 'matthew', 'daisy']
daisy
['raymond', 'rachel', 'matthew', 'susan', 'matthew']
raymond
-- Britney Spears
matthew
susan
matthew
susan
['raymond', 'rachel', 'matthew', 'susan']
['raymond', 'rachel', 'matthew', 'susan']
['rachel', 'matthew']
['matthew', 'susan', 'matthew']
['matthew', 'matthew', 'rachel', 'raymond', 'susan']
19210
19210
3
True
{40, 10, 20, 30}
{20, 30}
{10}
{40}
Yes, we can!
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
The answer is ٤٢ today
>>> # AF_INET  == ipv4
>>> # AF_INET6
>>> # SOCK_STREAM == tcp
>>> # SOCK_DGRAM = udp
>>> 
>>> 
>>> type(d1)
<class 'dict'>
>>> type(d2)
<class 'dict'>
>>> type(d3)
<class 'dict'>
>>> type(d4)
<class 'dict'>
>>> 
>>> d1
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
>>> d2
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
>>> d3
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
>>> d4
{'raymond': ['red'], 'rachel': ['blue'], 'matthew': ['yellow']}
>>> urllib.parse.parse_qs('host=171.0.15.3&port=8080&port=8081')
{'host': ['171.0.15.3'], 'port': ['8080', '8081']}
>>> x = 5 + 5
>>> x = 5 * 2
>>> 
>>> 
