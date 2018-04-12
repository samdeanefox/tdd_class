''' The minimum you need to follow the great Kent Beck
    and his magical example of teaching Python, and TDD,
    to build a unittest framework from scratch while
    using it.  Sounds crazy.
'''

def collatz(x):
    ''' Famous function in computer science
        for the Collatz conjecture which is
        the simplest known example of Halting Problem.

        >>> collatz(10)
        5
        >>> collatz(11)
        34

    '''
    if x % 2 == 0:
        return x // 2
    else:
        return 3*x + 1

class LivingThing:

    status = 'Alive'

class Unemployed(LivingThing):

    company = 'None'

class Employee(LivingThing):
    'Worker at a company'

    company = 'Cisco'

    def __init__(self, name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary

    def give_raise(self, percentage):
        self.salary = self.salary * (100 + percentage) // 100


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())

    vikas = Employee('Vikas Kokkalla', 'male', 35)
    craig = Employee('Craig Williams', 'male', 31)
    rucha = Employee('Rucha Gupte', 'female', 39)

    rucha.give_raise(20)        # ==> type(rucha).give_raise(rucha, 20)
    print(rucha.salary)

    print(vikas.gender)
    print(getattr(vikas, 'gender'))







