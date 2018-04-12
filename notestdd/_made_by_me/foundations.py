""" Goal: Learn a small but very useful subset of Python
    that will let us write our own test framework from scratch
    and practice TDD -- Test Driven Development
"""

def collatz(x):
    """ Famous function in computer science for that
    Collatz conjecture which is the simplest known example
    of the Halting problem

        >>> collatz(10)
        5
        >>> collatz(11)
        35
        >>> collatz('hello')
        Traceback (most recent call last):
            ...
        TypeError: not all arguments converted during string formatting

    """
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

assert collatz(10) == 5
assert collatz(11) == 34, 'short description'

try:
    collatz('hello')
except TypeError:
    pass
else:
    assert False, 'expected TypeError'
finally:
    print('done')

import doctest
print(doctest.testmod())


####################################################

class Employee:

    def __init__(self, name, salary, rank):
        self.name = name
        self.salary = salary
        self.rank = rank

    def give_raise(self, amount):
        self.salary += self.salary / (100/amount)