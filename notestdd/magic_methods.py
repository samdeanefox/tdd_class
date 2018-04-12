# The special methods are documented here:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# That is no fun to read, so you can use my brief executable notes below
# as a short-cut.

# Traditional math operators
print( 30 + 40, (30).__add__(40) )
print( 30 * 40, (30).__mul__(40) )
print( 38 / 5,  (38).__truediv__(5) )
print( 38 // 5, (38).__floordiv__(5) )
print( 30 ** 4, (30).__pow__(4) )

# Traditional bitwise operators
print( -30,     (30).__neg__() )
print( 30 & 40, (30).__and__(40) )
print( 30 | 40, (30).__or__(40) )
print( 30 & ~40, (30).__and__((40).__invert__()) )
print( 30 << 2, (30).__lshift__(2) )
print( 30 >> 2, (30).__rshift__(2) )

# Other operators
print('hello'[0], 'hello'.__getitem__(0))
print('el' in 'hello', 'hello'.__contains__('el'))

# Built-in functions
print(len('hello'), 'hello'.__len__())
print(str('hello'), 'hello'.__str__())
print(repr('hello'), 'hello'.__repr__())
print(abs(9+12j), (9+12j).__abs__())

# Built-in keywords -- How "for" works 

for x in [10, 20, 30]:
    print(x ** 2)

it = [10, 20, 30].__iter__()
while True:
    try:
        x = it.__next__()
    except StopIteration:
        break
    print(x ** 2)    

# Built-in keywords -- How "with" works

with open('notestdd/stocks.txt') as f:
    print(len(f.read()))

internal_object = open('notestdd/stocks.txt')
f = internal_object.__enter__()
try:
    print(len(f.read()))
finally:
    f.__exit__()









    
