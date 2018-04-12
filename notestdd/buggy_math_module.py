
'''
Quadratic Formula Stability:
    https://people.csail.mit.edu/bkph/articles/Quadratics.pdf 4ac is very small

Gentle cross-over to linear when a is small
    https://math.stackexchange.com/questions/866331                   a is close to zero

Hypoteneuse Stability:
    https://www.johndcook.com/blog/2010/06/02/whats-so-hard-about-finding-a-hypotenuse/

Kahan:
    https://people.eecs.berkeley.edu/~wkahan/Qdrtcs.pdf

Avoiding division by zero

Handling a == b == 0

Vieta's formulas:
    https://brilliant.org/wiki/vietas-formula/
'''

import cmath

def linear(b, c):
    'Solve bx + c = 0'
    if b == 0:
        if c == 0:
            return 0
        raise ValueError('A and B cannot both be zero with C as non-zero')
    return -c / b

def quadratic(a, b, c):
    if a == 0.0:
        return linear(b, c)
    root = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    return x1, x2
