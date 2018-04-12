''' Fast tour of the Python world.
    No time for details :-)
'''

import math

print( math.cos(3.0) )

from math import tan, log

print( tan(3.0), log(3.0) )

def square(x):
    'Return a value times itself'
    return x * x

print( square(11) )
print( [square(0), square(1), square(2), square(3), square(4)] )
print( list(map(square, range(10))) )
print( [x**2 for x in range(10)] )
print( list(map(lambda x: x**2, range(10))) )

######################################################

f = open('notestdd/stocks.txt')
try:
    data = f.read()
    print( len(data) )
finally:
    f.close()

with open('notestdd/stocks.txt') as f:
    data = f.read()
    print( len(data) )

#####################################################

from contextlib import suppress
import os

try:
    os.remove('xyzpdq.txt')
except FileNotFoundError:
    pass

with suppress(FileNotFoundError):
    os.remove('xyzpdq.txt')

#####################################################
# Dict    curly braces AND colons make a dictionary

brand = {
    'raymond': 'mac',
    'rachel': 'pc',
    'matthew': 'vtech',
}

print( type(brand) )
print( brand )
print( len(brand) )
print( brand['rachel'] )
print( 'rachel' in brand )

# EAFP -- Easier to ask forgiveness than permission
try:
    print( brand['susan'] )
except KeyError:
    print('Oops, I did it again')

# LBYL -- Look before you leap
if 'susan' in brand:
    print( brand['susan'] )
else:
    print('I made you believe')

# Unconditional lookup -- This always succeeds
print( brand.get('susan',  "we're more than just friends") )

print( brand.keys() )
print( brand.values() )
print( brand.items() )

#############################################################
# Lists     square brackets   mutable, ordered, and allows duplicates

names = ['raymond', 'rachel', 'matthew', 'susan', 'matthew']
print( type(names) )
print( len(names) )
print( names )

names.append('daisy')
print( names )
print( names.pop() )    # append/pop implement a LIFO stack
print( names )

print( names[0] )       # zero-indexed

try:
    print( names[50] )
except IndexError:
    print('-- Britney Spears')

print( names[len(names) - 1] )
print( names[len(names) - 2] )
print( names[-1] )
print( names[-2] )

print( [names[0], names[1], names[2], names[3]] )
print( names[:4] )      # list slicing gives you the first four
print( names[1:3] )     # 3 - 1 ==> 2
print( names[-3:] )     # last three

names.sort()
print(names)

## Logging ##############################################
#
# DEBUG INFO WARNING ERROR CRITICAL

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)-8s | %(asctime)s | %(message)s',
    filename = 'basics.log',
)

logging.debug('Executing line 122 and other boring details')
logging.info('The human head weight 8 and 1/2 pounds')
logging.warning('Running low on disk space')
logging.error('Oh no, the data input file is missing')
logging.critical('The CPU is melting')
try:
    print(32 / 0)
except ZeroDivisionError:
    logging.exception('Tried to divide 32')

## How to access the internet ############################

import urllib.request

u = urllib.request.urlopen('http://jython.org')
try:
    page = u.read()
    print(len(page))
finally:
    u.close()

with urllib.request.urlopen('http://jython.org') as u:
    page = u.read()
    print(len(page))

## Sets ##################################################
# Curly braces without colons makes sets!

s = {10, 20, 30, 20, 10}    # Sets eliminate duplicates
print( len(s) )
print( 20 in s )            # Fast membership testing
t = {20, 30, 40}
print( s.union(t) )         # Classic set-to-set operations
print( s.intersection(t) )
print( s.difference(t) )
print( t.difference(s) )

supported_extensions = {'css', 'php', 'html', 'xml', 'xhtml'}
url = 'http://www.cisco.com/forums/python/games.html'
extension = url.split('.')[-1]
if extension in supported_extensions:
    print('Yes, we can!')
else:
    print('Unsupported. Fake. SAD! Covfefe')

## Encoding and Decoding ########################################
#
#  Live Object --(encoding)-->   bytes  --(decoding)--> Live Object
#  Voice       mp3 au aiff wav -> file  ->               Voice
#  Unicode(str)   utf8 latin-1
#  Dict       pickle marshal yaml json url

# Encoders and Decoders come in pairs -> Codecs

s = 'The answer is \u0664\u0662 today'
print(s)
b1 = s.encode('utf-32')
b2 = s.encode('utf-16')
b3 = s.encode('utf-8')
print(b1.decode('utf-32'))
print(b2.decode('utf-16'))
print(b3.decode('utf-8'))

import json, pickle, urllib.parse, marshal

#color = {'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
color = dict(raymond='red', rachel='blue', matthew='yellow')

s1 = json.dumps(color)
s2 = pickle.dumps(color)
s3 = marshal.dumps(color)
s4 = urllib.parse.urlencode(color)

d1 = json.loads(s1)
d2 = pickle.loads(s2)
d3 = marshal.loads(s3)
d4 = urllib.parse.parse_qs(s4)
