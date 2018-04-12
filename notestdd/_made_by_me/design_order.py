""" Goal: Write a function that sums a cube and a square and subtracts
the n-th prime.

"""

########################################################
# Top Down Design

def f(x, n):
    "Sum a cude and square and subtract the n-th prime."
    return cube(x) + square(x) - nth_prime(n)

def cube(x):
    return 27

def square(x):
    return 9

def nth_prime(n):
    return 7

assert f(3, 4) == 29


########################################################
# Bottom-up Design

def cube(x):
    return x ** 3

assert cube(3) == 27

def square(x):
    return x * x

assert square(3) == 9

def nth_prime(n):
    primes = [2,3,5,7,11,13,17]
    return primes[n-1]

def f(x, n):
    "Sum a cude and square and subtract the n-th prime."
    return cube(x) + square(x) - nth_prime(n)

assert f(3, 4) == 29
