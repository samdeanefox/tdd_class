'Some module level docstring'

print('My name is', __name__)
print('What I like to do:')
print(__doc__)

# We take advantage of the __name__ assignments
# to determine whether a module was imported

def square(x):
    return x ** 2


if __name__ == '__main__':
    print('Woohoo! I was run directly.')
    print(square(5))
else:
    print('Oh no!  I was imported')
