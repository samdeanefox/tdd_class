"""Python Basics

Cover lots of 'em!

"""

from beck import TestCase, run_tests
import logging

logging.basicConfig(level=logging.INFO)

######################################################
# How numbers work

class TestNumbers(TestCase):

    def test_types(self):
        assert type(5) == int
        assert type(True) == bool
        assert type(1.23) == float
        assert type(4+5j) == complex

    def test_numbers(self):
        assert 1 == 1.0 == (1+0j) == True
        assert 0 == 0.0 == 0j == False

    def test_hierarchy(self):
        assert type(False + 2) == int
        assert type(3 + 4.56) == float
        assert type(7.89 + 10j) == complex

####################################################
# String Theory
class TestStrings(TestCase):

    def test_literals(self):
        assert 'hello' == 'hello'
        assert "don't" == 'don\'t' == """don't""" == '''don't'''
        assert len('\\') == 1
        assert len(r'\\') == 2

    def test_multiline(self):
        poem = """Roses are red,
        violents are blue,
        I program Python,
        you can too!"""
        assert len(poem.splitlines()) == 4

    def test_casers(self):
        s = 'i love Python'
        assert s.upper() == 'I LOVE PYTHON'
        assert s.lower() == 'i love python'
        assert s.title() == 'I Love Python'
        assert s.capitalize() == 'I love python'

    def test_predicates(self):
        assert 'love'.islower()
        assert 'PYTHON'.isupper()
        assert 'abc'.isalpha()
        assert '123'.isdigit()
        assert ' \t\r\n'.isspace

    def test_indexing(self):
        s = 'the tale of two cities'
        assert 'two' in s
        assert 'ale' in s
        assert s.index('the') == 0
        assert s.index('tale') == 4
        assert s[0] == 't' and s[1] == 'h' and s[2] == 'e'
        assert s[-1] == 's' and s[-2] == 'e' and s[-3] == 'i'
        assert s[:8] == 'the tale', 'first eight characters'
        assert s[-6:] == 'cities', 'the last six characters'
        assert s[9:11] == 'of'
        assert s[-10:-7] == 'two'
        with self.assert_raises(IndexError):
            s[100]

    def test_split_join(self):
        names = 'grant peter sam'
        assert type(names) == list
        assert type(names[0]) == str
        assert len(names) == 3
        assert ','.join(names) == 'grant,peter,sam'
        assert ''.join(names) == 'grantpetersam'

###################################################
# How to make functions

def cube(x):
    "Return a value times itself thrice"
    return x * x * x
# >>> help(cube)

pow3 = lambda x: x ** 3
pow3.__name__ = 'pow3'
pow3.__doc__ = 'Return x to the third power'

class TestFunctions(TestCase):

    def test_def(self):
        assert cube(5) == 125
        assert cube.__name__ == 'cube'
        assert cube.__doc__ == "Return a value times itself thrice"

    def test_lambda(self):
        assert pow3(7) == 343
        assert pow3.__name__ == 'pow3'
        assert pow3.__doc__ == 'Return x to the third power.'

################################################################
# How lists work
#
# Computer science: dyamic variant array of consecutive pointers
# Dynamic: can change its size
# Variant: it can hold different types
# Consecutive: efficient storage which is indexable
# Pointers: Python containers don't "contain" anything (just references)

class TestLists(TestCase):
    def test_indexing(self):
        plants = ['tree', 'shrub', 'cactus', 'climber']
        assert type(plants) == list
        assert len(plants) == 4
        assert  plants[0] == 'tree'
        assert plants[-1] == 'climber'
        assert plants[:] == ['tree', 'shrub', 'cactus', 'climber']

    def test_searchers(self):
        plants = ['tree', 'shrub', 'cactus', 'climber']
        assert 'shrub' in plants
        assert 'flower' not in plants
        assert plants.count('cactus') == 1
        assert plants.index('climber') == 3
        with self.assert_raises(ValueError):
            plants.index('flower')

    def test_adders(self):
        plants = ['tree', 'shrub', 'cactus', 'climber']
        plants.append('flower')
        assert len(plants) == 5
        more_plants = ['vine', 'bush']
        plants.extend(more_plants)
        assert len(plants) == 7
        plants.insert(0, 'flower')
        assert plants[0] == 'flower'

    def test_deleters(self):
        plants = ['tree', 'shrub', 'cactus', 'climber']
        del plants[0]
        assert len(plants) == 3
        assert plants.pop() == 'climber'
        assert len(plants) == 2
        plants.remove('cactus')
        assert len(plants) == 1
        plants.clear()
        assert len(plants) == 0

    def test_orderers(self):
        plants = ['tree', 'shrub', 'cactus', 'climber']
        plants.sort()
        assert plants[0] == 'cactus'
        plants.reverse()
        assert plants[0] == 'tree'

#################################################################
# Basics of dictionaries
#
# Mutable mapping data structure that is unbelievably fast and efficient
#
# Dict in Python 2.7 are in arbitrary but deterministic order
# Dict in 3.5 in randomized on every restart order.
# Dict in Python 3.6 in insertion order

class TestDicts(TestCase):

    def test_makers(self):
        colors = {'grant': 'orange', 'sam': 'blue', 'gerard': 'yellow'}
        assert type(colors) == dict
        colors = dict(grant='orange', sam='blue', gerard='yellow')
        assert type(colors) == dict

    def test_lookups(self):
        colors = {'grant': 'orange', 'sam': 'blue', 'gerard': 'yellow'}
        assert 'grant' in colors
        assert colors['grant'] == 'orange'
        assert colors.get('raymond', 'blue') == 'blue'
        colors['grant'] == 'blue'
        assert colors.get('grant', 'orange') == 'blue'
        with self.assert_raises(KeyError):
            colors['peter']

    def test_removers(self):
        colors = {'grant': 'orange', 'sam': 'blue', 'gerard': 'yellow'}
        del colors['sam']
        assert len(colors) == 2
        assert colors.pop('peter', 'black') == 'black'
        assert colors.pop('grant') == 'orange'
        assert len(colors) == 1
        assert colors.popitem() == ('gerard', 'yellow')
        assert len(colors) == 0
        colors.clear()

    def test_iterators(self):
        colors = {'grant': 'orange', 'sam': 'blue', 'gerard': 'yellow'}
        assert sorted(colors) == ['gerard', 'grant', 'sam']
        assert sorted(colors.keys()) == ['gerard', 'grant', 'sam']
        assert sorted(colors.values()) == ['blue', 'orange', 'yellow']
        assert sorted(colors.items()) == [
            ('gerard', 'yellow'),
            ('grant', 'orange'),
            ('sam', 'blue')
        ]

class TestSets(TestCase):

    def test_deduping(self):
        "Number one use case: deduping"
        j = {10, 20, 30, 20, 10}
        assert type(j) == set
        assert len(j) == 3
        k = set('abracadabra')
        assert len(k) == 5

    def test_membership(self):
        "Number two use case: membership testing."
        values = set(range(int(1e6)))
        assert 123456 in values

########################################################################
# How files work

class TestFiles(TestCase):
    def test_old_open_pattern(self):
        f = open('../hamlet.txt')
        try:
            data = f.read()
            assert len(data) > 0
        finally:
            f.close()
    def test_new_open_pattern(self):
        with open('../hamlet.txt') as f:
            data = f.read()
            assert len(data) > 0

#########################################################################
# How to access the internet

import urllib.request
class TestTubes(TestCase):
    def test_old_open_pattern(self):
        con = urllib.request.urlopen('http://jython.org')
        try:
            data = con.read()
            assert len(data) > 0
        finally:
            con.close()

    def test_new_open_pattern(self):
        with urllib.request.urlopen('http://jython.org') as con:
            data = con.read()
            assert len(data) > 0

########################################################################
# Encoding and decoding objects
#
# Encoder/decoder pair is called a codec

class TestEncodeDecode(TestCase):
    def test_strings(self):
        s = 'I am feeling \N{white smiling face} today'
        assert type(s) == str
        assert len(s) == 21
        b1 = s.encode('utf-8)
        b2 = s.encode('utf-16')
        b3 = s.encode('utf-32')
        assert type(b1) == type(b2) == type(b3) == bytes
        assert len(b1) == 23
        assert len(b2) == 44
        assert len(b3) == 48
        s1 = b1.decode('utf-8')
        s2 = b2.decode('utf-16')
        s3 = b3.decode('utf-32')
        assert s == s1 == s2 == s3

    def test_objects(self):
        import json, pickle, urllib.parse
        cars = {'Rajesh': 'electric', 'Nima': 'beetle', 'Sam', 'Toyota'}
        s1 = json.dumps(cars)
        assert type(s1) == str
        d1 = json.loads(s1)
        assert cars == d1
        b1 = pickle.dumps(cars)
        assert type(b1) == bytes
        d2 = pickle.loads(b1)
        assert cars == d2
        s2 = urllib.parse.urlencode(cars)
        assert type(s2) == str
        d3 = urllib.parse.parse_qs(s2)
        assert d3 = {'Rajesh': ['electric'], 'Nima': ['beetle'], 'Sam', ['Toyota']}

# Urlencoding RFC 1738
#   Specific to URLs. Handles only simple dicts with string keys and values.
#   Oddly, allows multiple uses of the same key
# JSON
#   Simple spec, commonly implemented. Works with variety of programming languages
# Pickle
#   Python specific. Handles a huge variety of Python types.
# YAML
#   Complex spec is much easier to read/write by humans.
# XML
#   Complex spec but is very feature complete and rich, powerful toolchain

                      


if __name__ == '__main__':
    print('%s in %.6f seconds' % run_tests(TestNumbers))
    print('%s in %.6f seconds' % run_tests(TestStrings))
    print('%s in %.6f seconds' % run_tests(TestFunctions))
    print('%s in %.6f seconds' % run_tests(TestLists))
    print('%s in %.6f seconds' % run_tests(TestDicts))
    print('%s in %.6f seconds' % run_tests(TestSets))
    print('%s in %.6f seconds' % run_tests(TestFiles))
    print('%s in %.6f seconds' % run_tests(TestTubes))
    print('%s in %.6f seconds' % run_tests(TestEncodeDecode))
