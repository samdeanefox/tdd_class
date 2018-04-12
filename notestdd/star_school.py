'Learn common argument passing patterns'

def mypow(base, exp):
    'Compute base to the power of exp'
    return base ** exp

print( mypow(2, 5) )                        # Positional arg -- order matters
print( mypow(exp=5, base=2) )               # Keyword arg -- name that matters
print( mypow(2, exp=5) )                    # Hybrid -- RULE:  positional arguments go BEFORE keyword args

arguments = (2, 5)                          # Cheap luggage -- Tuple are compact and fast ordered collections
print( mypow(arguments[0], arguments[1]) )  # TSA demands that you unpack your luggage
print( mypow(*arguments) )                  # 1 star in a function call UNPACKS any SEQUENCE into POSITIONAL arguments

arguments = {'exp': 5, 'base': 2}           # Expensive luggage -- Dicts are sparse.  You get to lookup by name.
print( mypow(exp=arguments['exp'], base=arguments['base']) )   # TSA demands that you unpack your luggage
print( mypow(**arguments) )                 # 2 stars in a function call UNPACKS any MAPPING into KEYWORD arguments

def f(a, b, c=0, d=0):                      # Losing battle!  RULE: required arguments go before optional arguments with defaults
    return a + b + c + d

def g(a, b, *args, **kwargs):               # 1 star in a function definition PACKS the POSITIONAL arguments into a TUPLE
    print(a, b, args, kwargs)               # 2 stasr in a function definition PACKS the KEYWORD arguments into a DICT

g(10, 20, 30, 40, x=1, y=2, z=3) 

orig_pow = mypow                            # Step 1:  Save the original function

def logging_mypow(*args, **kwargs):         # Step 2:  Write a wrapper
    'Wrap mypow() to add input and output logging'
    print('Called mypow() with %r and %r' % (args, kwargs))
    answer = orig_pow(*args, **kwargs)
    print('The answer is %r' % answer)
    return answer

mypow = logging_mypow                       # Step 3:  Replace mypow() with the new logging function

x = mypow(2, 5)
x = mypow(exp=5, base=2)
x = mypow(2, exp=5)

from pprint import pprint

m = [ [10, 20, 30], [40, 50, 60] ]          # 2 rows and 3 columns
pprint(m, width=15)
t = list(zip(*m))                           # Way to transpose data
pprint(t, width=12)
