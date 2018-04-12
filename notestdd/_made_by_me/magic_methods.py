"""Learn about Magic Methods aka Special Methods aka Dunder Methods

Everything is documented here:
https://docs.python.org/3/reference/datamodel.html

That is no fun to read, so you can use my brief executable notes
below as a shortcut.

"""

# Traditional math operators

print(30 + 40, (30).__add__(40))
print(30 * 40, (30).__mul__(40))
print(30 / 40, (30).__truediv__(40))
print(30 // 40, (30).__floordiv__(40))
print(30 ** 5, (30).__pow__(5))

# Traditional bitwise operators

print(-30, (30).__neg__())
print(30 & 40, (30).__and__(40))
print(30 | 40, (30).__or__(40))
print(~30, (30).__invert__())
print(30 << 2, (30).__lshift__(2))

# Other operators

print('hello'[0], 'hello'.__getitem__(0))
print('el' in 'hello', 'hello'.__contains__('el'))

# Built-in functions
print(len('hello'), 'hello'.__len__())
print(str(0), (0).__str__())

# Built-in statements -- how "for" works
for x in [10, 20, 30]:
    print(x ** 2)

it = iter([10,20,30])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    print(x ** 2)

# How print works

print(10)

import sys
sys.stdout.write(str(10) + '\n')

# How with works

with open('../hamlet.txt') as f:
    print(f.read())

internal_object = open('../hamlet.txt')
f = internal_object.__enter__()
try:
    print(len(f.read()))
finally:
    f.__exit__()
