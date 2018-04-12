Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # casers:    upper lower title capitalize swapcase
>>> # predicates:   'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',     startswith endswith
>>> # searchers:   x in s      s.find(x)      s.index(x)
>>> # aligners:    ljust    rjust    zfill     center
>>> # torn/restored:   split   join   replace   partition
>>> s = 'the tale of two cities'
>>> s.upper()
'THE TALE OF TWO CITIES'
>>> s.capitalize()
'The tale of two cities'
>>> s.title()
'The Tale Of Two Cities'
>>> s.lower()
'the tale of two cities'
>>> s.title().swapcase()
'tHE tALE oF tWO cITIES'
>>> "don't ever trust title".title()
"Don'T Ever Trust Title"
>>> s.islower()
True
>>> 'HELLO'.isupper()
True
>>> s.startswith('the')
True
>>> s.endswith('ties')
True
>>> s = 'the tale of two cities'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s = 'the tale of two cities'
>>> 'tale' in s
True
>>> 'ale' in s
True
>>> ping_result = '20 packets sent. 20 packets received. 0.0% loss rate'
>>> assert '0.0%' in ping_result
>>> ping_result = '20 packets sent. 10 packets received. 50.0% loss rate'
>>> assert '0.0%' in ping_result
>>> 
>>> device_status 'Status:  connected'
SyntaxError: invalid syntax
>>> device_status = 'Status:  connected'
>>> assert 'connected' in device_status
>>> device_status = 'Status:  disconnected'
>>> 
>>> 
>>> s.find('tale')
4
>>> s.find('e')
2
>>> s.find('e', 3)
7
>>> 30 + 40
70
>>> _ * 10
700
>>> _ * 10
7000
>>> _ * 10
70000
>>> i = -1
>>> s
'the tale of two cities'
>>> i = s.find('e', i+1); print(i)
2
>>> i = s.find('e', i+1); print(i)
7
>>> i = s.find('e', i+1); print(i)
20
>>> i = s.find('e', i+1); print(i)
-1
>>> s
'the tale of two cities'
>>> s.find('e')
2
>>> s.rfind('e')
20
>>> s
'the tale of two cities'
>>> s.replace('two', 'three')
'the tale of three cities'
>>> s
'the tale of two cities'
>>> s.replace('two', 'three')
'the tale of three cities'
>>> s
'the tale of two cities'
>>> t = s.replace('two', 'three')
>>> s
'the tale of two cities'
>>> t
'the tale of three cities'
>>> x = 10
>>> x + 1
11
>>> x
10
>>> x = x + 1
>>> 
>>> s.upper()
'THE TALE OF TWO CITIES'
>>> s
'the tale of two cities'
>>> s.center(50)
'              the tale of two cities              '
>>> s
'the tale of two cities'
>>> 
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> for method_name in dir(str):
	print(method_name)

	
__add__
__class__
__contains__
__delattr__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mod__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmod__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
capitalize
casefold
center
count
encode
endswith
expandtabs
find
format
format_map
index
isalnum
isalpha
isdecimal
isdigit
isidentifier
islower
isnumeric
isprintable
isspace
istitle
isupper
join
ljust
lower
lstrip
maketrans
partition
replace
rfind
rindex
rjust
rpartition
rsplit
rstrip
split
splitlines
startswith
strip
swapcase
title
translate
upper
zfill
>>> for method_name in dir(str):
	if method_name.startswith('__'):
		print(method_name)

		
__add__
__class__
__contains__
__delattr__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mod__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmod__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
>>> 
>>> s
'the tale of two cities'
>>> t = s.split()
>>> t
['the', 'tale', 'of', 'two', 'cities']
>>> ''.join(t)
'thetaleoftwocities'
>>> ' '.join(t)
'the tale of two cities'
>>> ' <--> '.join(t)
'the <--> tale <--> of <--> two <--> cities'
>>> ' + '.join(t)
'the + tale + of + two + cities'
>>> 
>>> s
'the tale of two cities'
>>> s.center(50)
'              the tale of two cities              '
>>> s.ljust(50)
'the tale of two cities                            '
>>> s.rjust(50)
'                            the tale of two cities'
>>> 
>>> s.center(50, '*')
'**************the tale of two cities**************'
>>> 
>>> s.center(len(s) + 2)
' the tale of two cities '
>>> s
'the tale of two cities'
>>> s.center(len(s) + 2).center(50, '=').title()
'============= The Tale Of Two Cities ============='
>>> 10 + 5 - 1 + 3
17
>>> (10).__add__(5).__sub__(1).__add__(3)
17
>>> s = 'www.python.org'
>>> s.partition('.')
('www', '.', 'python.org')
>>> s.rpartition('.')
('www.python', '.', 'org')
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
..
2 run, 1 failed
>>> 
>>> dir(TestMinimumClasses)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'run', 'set_up', 'tear_down', 'test_employee', 'test_employee_neg_raise']
>>> for method_name in dir(TestMinimumClasses):
	print(method_name)

	
__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
__weakref__
run
set_up
tear_down
test_employee
test_employee_neg_raise
>>> for method_name in dir(TestMinimumClasses):
	if method_name.startswith('test_'):
		print(method_name)

		
test_employee
test_employee_neg_raise
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 35, in <module>
    beck.run_tests(TestMinimumClasses)
TypeError: run_tests() missing 1 required positional argument: 'test_method_names'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 35, in <module>
    beck.run_tests(TestMinimumClasses)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 80, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 69, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
TypeError: __init__() missing 2 required positional arguments: 'method_name' and 'result'
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
INFO:root:Test succeeded: test_employee
.ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 29, in test_employee_neg_raise
    assert navra.salary == 185
AssertionError
.
2 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 29, in test_employee_neg_raise
    assert navra.salary == 185      # Intentionally failing test
AssertionError
.
1 run, 1 failed
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py 
INFO:root:Test succeeded: test_employee
.ERROR:root:Test failed: test_employee_neg_raise
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_the_minimum_with_beck_framework.py", line 29, in test_employee_neg_raise
    assert navra.salary == 185      # Intentionally failing test
AssertionError
.
2 run, 1 failed
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2379
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-2379
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Jones,David,Transport Specialist,djones@example.com,559-555-1892
Davis,Harold,Quality Assurance Tech,hdavis@example.com,559-555-1478
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2379
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-2379
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Jones,David,Transport Specialist,djones@example.com,559-555-1892
Davis,Harold,Quality Assurance Tech,hdavis@example.com,559-555-1478
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300

Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318

Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348

Jones,David,Grape Ager,david@example.com,559-555-2379

Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301

Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2379

Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397

Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-2379

Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513

Jones,David,Transport Specialist,djones@example.com,559-555-1892

Davis,Harold,Quality Assurance Tech,hdavis@example.com,559-555-1478

Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> # 1) "print" is adding a newline 2) orig line has a newline
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2379
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-2379
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Jones,David,Transport Specialist,djones@example.com,559-555-1892
Davis,Harold,Quality Assurance Tech,hdavis@example.com,559-555-1478
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> s = '   three    blind    mice   '
>>> s.strip()
'three    blind    mice'
>>> s.lstrip()
'three    blind    mice   '
>>> s.rstrip()
'   three    blind    mice'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212

Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300

Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318

Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348

Jones,David,Grape Ager,david@example.com,559-555-2379

Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301

Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2379

Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397

Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-2379

Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513

Jones,David,Transport Specialist,djones@example.com,559-555-1892

Davis,Harold,Quality Assurance Tech,hdavis@example.com,559-555-1478

Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700

>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> line.rstrip()
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700\n'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
Masterson,Martin,Asst Raisin Smusher,martin@example.com,559-555-2348
Jones,David,Grape Ager,david@example.com,559-555-2379
Zapata,Luis,VP Grape Sales,luis@example.com,559-555-2301
Gunter,Fritz,Grape Smusher,fritz@example.com,559-555-2379
Pichon,Esmerela,Head Raisin Counter,esmerelda@example.com,559-555-2397
Blain,Marilyn,Raisin Packager,marilyn@example.com,559-555-2379
Marks,Blair,VP Investor Relations,blair@example.com,559-555-6513
Jones,David,Transport Specialist,djones@example.com,559-555-1892
Davis,Harold,Quality Assurance Tech,hdavis@example.com,559-555-1478
Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700
>>> 
>>> 
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
['Hettinger,Raymond,VP', 'Raisin', 'Smushing,raymond@example.com,559-555-1212']
['Thomas,Mary,Sr.', 'Associate', 'Raisin', 'Design,mary@example.com,559-555-2300']
['Davis,Harold,Chief', 'Raisin', 'Picker,harold@example.com,559-555-2318']
['Masterson,Martin,Asst', 'Raisin', 'Smusher,martin@example.com,559-555-2348']
['Jones,David,Grape', 'Ager,david@example.com,559-555-2379']
['Zapata,Luis,VP', 'Grape', 'Sales,luis@example.com,559-555-2301']
['Gunter,Fritz,Grape', 'Smusher,fritz@example.com,559-555-2379']
['Pichon,Esmerela,Head', 'Raisin', 'Counter,esmerelda@example.com,559-555-2397']
['Blain,Marilyn,Raisin', 'Packager,marilyn@example.com,559-555-2379']
['Marks,Blair,VP', 'Investor', 'Relations,blair@example.com,559-555-6513']
['Jones,David,Transport', 'Specialist,djones@example.com,559-555-1892']
['Davis,Harold,Quality', 'Assurance', 'Tech,hdavis@example.com,559-555-1478']
['Schmidt,Gertrude,VP', 'Business', 'Development,gertrude@example.com,559-555-6700']
>>> 
>>> 
>>> line
'Schmidt,Gertrude,VP Business Development,gertrude@example.com,559-555-6700'
>>> fields
['Schmidt,Gertrude,VP', 'Business', 'Development,gertrude@example.com,559-555-6700']
>>> fields[0]
'Schmidt,Gertrude,VP'
>>> fields[1]
'Business'
>>> fields[2]
'Development,gertrude@example.com,559-555-6700'
>>> help(str.split)
Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
['Hettinger', 'Raymond', 'VP Raisin Smushing', 'raymond@example.com', '559-555-1212']
['Thomas', 'Mary', 'Sr. Associate Raisin Design', 'mary@example.com', '559-555-2300']
['Davis', 'Harold', 'Chief Raisin Picker', 'harold@example.com', '559-555-2318']
['Masterson', 'Martin', 'Asst Raisin Smusher', 'martin@example.com', '559-555-2348']
['Jones', 'David', 'Grape Ager', 'david@example.com', '559-555-2379']
['Zapata', 'Luis', 'VP Grape Sales', 'luis@example.com', '559-555-2301']
['Gunter', 'Fritz', 'Grape Smusher', 'fritz@example.com', '559-555-2379']
['Pichon', 'Esmerela', 'Head Raisin Counter', 'esmerelda@example.com', '559-555-2397']
['Blain', 'Marilyn', 'Raisin Packager', 'marilyn@example.com', '559-555-2379']
['Marks', 'Blair', 'VP Investor Relations', 'blair@example.com', '559-555-6513']
['Jones', 'David', 'Transport Specialist', 'djones@example.com', '559-555-1892']
['Davis', 'Harold', 'Quality Assurance Tech', 'hdavis@example.com', '559-555-1478']
['Schmidt', 'Gertrude', 'VP Business Development', 'gertrude@example.com', '559-555-6700']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
BEGIN:VCARD
VERSION:2.1
N:Gump;Forrest;;Mr.
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;GIF:http://www.example.com/dir_photos/my_photo.gif
TEL;WORK;VOICE:(111) 555-1212
TEL;HOME;VOICE:(404) 555-1212
ADR;WORK;PREF:;;100 Waters Edge;Baytown;LA;30314;United States of America
LABEL;WORK;PREF;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:100 Waters Edge=0D=
 =0ABaytown\, LA 30314=0D=0AUnited States of America
ADR;HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;HOME;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:42 Plantation St.=0D=0A=
 Baytown, LA 30314=0D=0AUnited States of America
EMAIL:forrestgump@example.com
REV:20080424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/vcard.py", line 26, in <module>
    print(vcard.format(lname=lname, fname=fname, title=title, email=email, phone=phone))
NameError: name 'vcard' is not defined
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
>>> 
>>> 'The answer is {0} today but was {1} yesterday'
'The answer is {0} today but was {1} yesterday'
>>> 'The answer is {0} today but was {1} yesterday'.format(10, 20)
'The answer is 10 today but was 20 yesterday'
>>> 'The answer is {1} today but was {1} yesterday'.format(10, 20)
'The answer is 20 today but was 20 yesterday'
>>> 'The answer is {1} today but was {0} yesterday'.format(10, 20)
'The answer is 20 today but was 10 yesterday'
>>> 'The answer is {new} today but was {old} yesterday'.format(old=10, new=20)
'The answer is 20 today but was 10 yesterday'
>>> 
>>> 'The answer is {new} today but was {old} yesterday'.format(old='bad', new='good')
'The answer is good today but was bad yesterday'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20170424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/vcard.py", line 29, in <module>
    vcard.write(vcard)
AttributeError: 'str' object has no attribute 'write'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20170424T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Wrote: Raymond_Hettinger.vcf
Wrote: Mary_Thomas.vcf
Wrote: Harold_Davis.vcf
Wrote: Martin_Masterson.vcf
Wrote: David_Jones.vcf
Wrote: Luis_Zapata.vcf
Wrote: Fritz_Gunter.vcf
Wrote: Esmerela_Pichon.vcf
Wrote: Marilyn_Blain.vcf
Wrote: Blair_Marks.vcf
Wrote: David_Jones.vcf
Wrote: Harold_Davis.vcf
Wrote: Gertrude_Schmidt.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
Wrote: Raymond_Hettinger.vcf
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Mary_Thomas.vcf
BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Harold_Davis.vcf
BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Martin_Masterson.vcf
BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20170424T195243Z
END:VCARD

Wrote: David_Jones.vcf
BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Luis_Zapata.vcf
BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Fritz_Gunter.vcf
BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Esmerela_Pichon.vcf
BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Marilyn_Blain.vcf
BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Blair_Marks.vcf
BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20170424T195243Z
END:VCARD

Wrote: David_Jones.vcf
BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Harold_Davis.vcf
BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20170424T195243Z
END:VCARD

Wrote: Gertrude_Schmidt.vcf
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20170424T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: Raymond_Hettinger.vcf
INFO:root:Wrote: Mary_Thomas.vcf
INFO:root:Wrote: Harold_Davis.vcf
INFO:root:Wrote: Martin_Masterson.vcf
INFO:root:Wrote: David_Jones.vcf
INFO:root:Wrote: Luis_Zapata.vcf
INFO:root:Wrote: Fritz_Gunter.vcf
INFO:root:Wrote: Esmerela_Pichon.vcf
INFO:root:Wrote: Marilyn_Blain.vcf
INFO:root:Wrote: Blair_Marks.vcf
INFO:root:Wrote: David_Jones.vcf
INFO:root:Wrote: Harold_Davis.vcf
INFO:root:Wrote: Gertrude_Schmidt.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: 559-555-1212.vcf
INFO:root:Wrote: 559-555-2300.vcf
INFO:root:Wrote: 559-555-2318.vcf
INFO:root:Wrote: 559-555-2348.vcf
INFO:root:Wrote: 559-555-2379.vcf
INFO:root:Wrote: 559-555-2301.vcf
INFO:root:Wrote: 559-555-2379.vcf
INFO:root:Wrote: 559-555-2397.vcf
INFO:root:Wrote: 559-555-2379.vcf
INFO:root:Wrote: 559-555-6513.vcf
INFO:root:Wrote: 559-555-1892.vcf
INFO:root:Wrote: 559-555-1478.vcf
INFO:root:Wrote: 559-555-6700.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond@example.com.vcf
INFO:root:Wrote: mary@example.com.vcf
INFO:root:Wrote: harold@example.com.vcf
INFO:root:Wrote: martin@example.com.vcf
INFO:root:Wrote: david@example.com.vcf
INFO:root:Wrote: luis@example.com.vcf
INFO:root:Wrote: fritz@example.com.vcf
INFO:root:Wrote: esmerelda@example.com.vcf
INFO:root:Wrote: marilyn@example.com.vcf
INFO:root:Wrote: blair@example.com.vcf
INFO:root:Wrote: djones@example.com.vcf
INFO:root:Wrote: hdavis@example.com.vcf
INFO:root:Wrote: gertrude@example.com.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> import requests
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
E
======================================================================
ERROR: test_quadratic (__main__.TestMathStuff)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package.py", line 10, in test_quadratic
    x1, x2 = quadratic(a, b, c)
NameError: name 'quadratic' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.017s

FAILED (errors=1)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
.
----------------------------------------------------------------------
Ran 1 test in 0.026s

OK
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
E
======================================================================
ERROR: test_quadratic (__main__.TestMathStuff)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package.py", line 10, in test_quadratic
    x1, x2 = buggy_math_module.quadratic(a, b, c)
  File "/Users/raymond/Dropbox/Public/sj164/buggy_math_module.py", line 6, in quadratic
    x2 = (-b - root) / (2 * a) / 0
ZeroDivisionError: float division by zero

----------------------------------------------------------------------
Ran 1 test in 0.015s

FAILED (errors=1)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/buggy_math_module.py =====
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
E
======================================================================
ERROR: test_quadratic (__main__.TestMathStuff)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package.py", line 11, in test_quadratic
    self.assertEqual(a*x1**2 + b*x + c, 0)
NameError: name 'x' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.014s

FAILED (errors=1)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
.
----------------------------------------------------------------------
Ran 1 test in 0.025s

OK
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
.
----------------------------------------------------------------------
Ran 1 test in 0.015s

OK
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/buggy_math_module.py =====
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
F
======================================================================
FAIL: test_quadratic (__main__.TestMathStuff)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package.py", line 11, in test_quadratic
    self.assertEqual(a*x1**2 + b*x1 + c, 0)
AssertionError: 330.0 != 0

----------------------------------------------------------------------
Ran 1 test in 0.022s

FAILED (failures=1)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
F
======================================================================
FAIL: test_quadratic (__main__.TestMathStuff)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package.py", line 12, in test_quadratic
    self.assertEqual(a*x2**2 + b*x2 + c, 0)
AssertionError: 1014.0 != 0

----------------------------------------------------------------------
Ran 1 test in 0.030s

FAILED (failures=1)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
.
----------------------------------------------------------------------
Ran 1 test in 0.019s

OK
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/buggy_math_module.py =====
>>> quadratic(8, -14, -15)
(2.5, -0.75)
>>> b**2
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    b**2
NameError: name 'b' is not defined
>>> 14**2
196
>>> 8 * 15
120
>>> quadratic(10, -14, 20)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    quadratic(10, -14, 20)
  File "/Users/raymond/Dropbox/Public/sj164/buggy_math_module.py", line 4, in quadratic
    root = math.sqrt(b**2 - 4*a*c)
ValueError: math domain error
>>> (-14) ** 2
196
>>> 4 * 10 * 20
800
>>> 196 - 800
-604
>>> math.sqrt(-604)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    math.sqrt(-604)
ValueError: math domain error
>>> math.sqrt(604)
24.576411454889016
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/buggy_math_module.py =====
>>> quadratic(10, -14, 20)
((0.7+1.2288205727444508j), (0.7-1.2288205727444508j))
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
>>> test_quad(8, -14, -15)
>>> test_quad(8, 0, -15)
>>> test_quad(8, 1, -15)
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
>>> test_quad()
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    test_quad()
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 6, in test_quad
    def test_quad(a, b, c):
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 626, in wrapped_test
    generator_kwargs, argspec, test, settings
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 428, in process_arguments_to_given
    lambda args: dict(args, **kwargs)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/strategies.py", line 130, in map
    pack=pack, strategy=self
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/strategies.py", line 253, in __init__
    self.is_empty = strategy.is_empty
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/deferred.py", line 72, in is_empty
    return self.wrapped_strategy.is_empty
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/deferred.py", line 81, in wrapped_strategy
    for k, v in self.__kwargs.items()})
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/strategies.py", line 584, in fixed_dictionaries
    check_strategy(v)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/strategies.py", line 1299, in check_strategy
    check_type(SearchStrategy, arg)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/strategies.py", line 1295, in check_type
    % (typ_string, name, arg, type(arg).__name__))
hypothesis.errors.InvalidArgument: Expected SearchStrategy but got <function floats at 0x1045c31e0> (type=function)
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 13, in <module>
    test_quad()
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 6, in test_quad
    def test_quad(a, b, c):
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 626, in wrapped_test
    generator_kwargs, argspec, test, settings
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 428, in process_arguments_to_given
    lambda args: dict(args, **kwargs)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/strategies.py", line 130, in map
    pack=pack, strategy=self
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/strategies.py", line 253, in __init__
    self.is_empty = strategy.is_empty
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/deferred.py", line 72, in is_empty
    return self.wrapped_strategy.is_empty
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/searchstrategy/deferred.py", line 81, in wrapped_strategy
    for k, v in self.__kwargs.items()})
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/strategies.py", line 584, in fixed_dictionaries
    check_strategy(v)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/strategies.py", line 1299, in check_strategy
    check_type(SearchStrategy, arg)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/strategies.py", line 1295, in check_type
    % (typ_string, name, arg, type(arg).__name__))
hypothesis.errors.InvalidArgument: Expected SearchStrategy but got <function floats at 0x104ec4268> (type=function)
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
Falsifying example: test_quad(a=0.0, b=0.0, c=0.0)
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 13, in <module>
    test_quad()
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 6, in test_quad
    def test_quad(a, b, c):
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 648, in wrapped_test
    state.run()
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 542, in run
    print_example=True, is_final=True
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/executors.py", line 58, in default_new_style_executor
    return function(data)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 111, in run
    return test(*args, **kwargs)
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 7, in test_quad
    x1, x2 = quadratic(a, b, c)
  File "/Users/raymond/Dropbox/Public/sj164/buggy_math_module.py", line 5, in quadratic
    x1 = (-b + root) / (2 * a)
ZeroDivisionError: complex division by zero
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
Falsifying example: test_quad(a=0.1, b=0.0, c=5e-324)
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 14, in <module>
    test_quad()
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 6, in test_quad
    def test_quad(a, b, c):
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 648, in wrapped_test
    state.run()
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 542, in run
    print_example=True, is_final=True
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/executors.py", line 58, in default_new_style_executor
    return function(data)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 111, in run
    return test(*args, **kwargs)
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 9, in test_quad
    assert a*x1**2 + b*x1 + c == 0.0
AssertionError
>>> 
 RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py 
Falsifying example: test_quad(a=2.0, b=0.0, c=0.5625)
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 15, in <module>
    test_quad()
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 6, in test_quad
    def test_quad(a, b, c):
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 648, in wrapped_test
    state.run()
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 542, in run
    print_example=True, is_final=True
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/executors.py", line 58, in default_new_style_executor
    return function(data)
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/hypothesis/core.py", line 111, in run
    return test(*args, **kwargs)
  File "/Users/raymond/Dropbox/Public/sj164/test_math_package_with_hypothesis.py", line 10, in test_quad
    assert a*x1**2 + b*x1 + c == 0.0
AssertionError
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/test_math_package.py =====
.
----------------------------------------------------------------------
Ran 1 test in 0.026s

OK
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
>>> 
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
8
>>> bin(30)
'0b11110'
>>> bin(40)
'0b101000'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
8 8
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
8 8
62 62
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
8 8
62 62
22 22
>>> bin(30)
'0b11110'
>>> bin(30 << 2)
'0b1111000'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
8 8
62 62
22 22
120 32985348833280
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
>>> bin(30)
'0b11110'
>>> bin(30 >> 2)
'0b111'
>>> 38 / 5
7.6
>>> 38 // 5
7
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
>>> s = 'hello'
>>> s[0]
'h'
>>> 
>>> 'el' in 'hello'
True
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
>>> len('hello')
5
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
5 5
>>> s = 35+7j
>>> str(s)
'(35+7j)'
>>> repr(s)
'(35+7j)'
>>> 
>>> 
>>> s = 'hello'
>>> str(s)
'hello'
>>> repr(s)
"'hello'"
>>> 
>>> print(s)
hello
>>> print(repr(s))
'hello'
>>> 
>>> 30 + 40
70
>>> print(30 + 40)
70
>>> '7' + '0'
'70'
>>> print('7' + '0')
70
>>> 
>>> 
>>> (30 + 40)
70
>>> (30 + 40) * 5
350
>>> ('7' + '0')
'70'
>>> ('7' + '0') * 5
'7070707070'
>>> # str() is used by print and is typically pretty
>>> #       for the end-user
>>> # repr() is used by interatice prompt
>>> #       it is less pretty, but more informative
>>> #       for the programmer
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
5 5
hello hello
'hello' 'hello'
>>> 
>>> abs(-3)
3
>>> abs(3-4j)
5.0
>>> abs(9-12j)
15.0
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(complex)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
5 5
hello hello
'hello' 'hello'
15.0 15.0
>>> 
>>> 
>>> s = [10, 20, 30]
>>> for x in s:
	print(x, x**2)

	
10 100
20 400
30 900
>>> it = iter(s)
>>> it
<list_iterator object at 0x1034a3400>
>>> next(it)
10
>>> next(it)
20
>>> next(it)
30
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    next(it)
StopIteration
>>> s = [10, 20, 30]
>>> it = s.__iter__()
>>> it
<list_iterator object at 0x1033d42e8>
>>> it.__next__()
10
>>> 
>>> 
>>> for x in s:
	print(x, x**2)

	
10 100
20 400
30 900
>>> it = s.__iter__()
>>> while True:
	try:
		x = it.__next__()
	except StopIteration:
		break
	print(x, x**2)

	
10 100
20 400
30 900
>>> f = open('notestdd/stocks.txt')
>>> for line in f:
	print(len(line), line, end='')

	
15 CSCO,100,18.04
15 ANTM,200,45.03
15 CSCO,150,19.05
15 MSFT,250,80.56
14 IBM,500,22.01
15 ANTM,250,44.23
16 GOOG,200,501.45
15 CSCO,175,19.56
14 MSFT,75,80.81
16 GOOG,300,502.65
14 IBM,150,25.01
>>> f = open('notestdd/stocks.txt')
>>> it = f.__iter__()
>>> while True:
	try:
		line = it.__next__()
	except StopIteration:
		break
	print(len(line), line, end='')

	
15 CSCO,100,18.04
15 ANTM,200,45.03
15 CSCO,150,19.05
15 MSFT,250,80.56
14 IBM,500,22.01
15 ANTM,250,44.23
16 GOOG,200,501.45
15 CSCO,175,19.56
14 MSFT,75,80.81
16 GOOG,300,502.65
14 IBM,150,25.01
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
5 5
hello hello
'hello' 'hello'
15.0 15.0
100
400
900
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
5 5
hello hello
'hello' 'hello'
15.0 15.0
100
400
900
100
400
900
>>> 
>>> 
>>> with open('notestdd/stocks.txt') as f:
	print(len(f.read()))

	
164
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/magic_methods.py =======
70 70
1200 1200
7.6 7.6
7 7
810000 810000
-30 -30
8 8
62 62
22 22
120 120
7 7
h h
True True
5 5
hello hello
'hello' 'hello'
15.0 15.0
100
400
900
100
400
900
164
164
>>> 30 + 40 - 5 + 1
66
>>> (30).__add__(40).__sub__(5).__add__(1)
66
>>> import threading
>>> printer_lock = threading.Lock()
>>> 
>>> printer_lock.acquire()
True
>>> print('Critical section 1')
Critical section 1
>>> print('Critical section 2')
Critical section 2
>>> printer_lock.release()
>>> 
>>> with printer_lock:
	print('Critical section 1')
	print('Critical section 2')

	
Critical section 1
Critical section 2
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
>>> s = [10, 20]
>>> len(s)
2
>>> suite.xyz
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    suite.xyz
AttributeError: 'TestSuite' object has no attribute 'xyz'
>>> suite.__len__
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    suite.__len__
AttributeError: 'TestSuite' object has no attribute '__len__'
>>> len(suite)
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    len(suite)
TypeError: object of type 'TestSuite' has no len()
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 59, in <module>
    assert len(suite) == 2
TypeError: object of type 'TestSuite' has no len()
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
>>> len(suite)
2
>>> suite.__len__()
2
>>> suite.cases
[(<class '__main__.TestMathFunctions'>, 'test_add'), (<class '__main__.TestMathFunctions'>, 'test_sub')]
>>> len(suite.cases)
2
>>> suite.cases[0]
(<class '__main__.TestMathFunctions'>, 'test_add')
>>> suite.cases[0][1]
'test_add'
>>> suite.cases[0]
(<class '__main__.TestMathFunctions'>, 'test_add')
>>> suite.cases.__getitem__(0)
(<class '__main__.TestMathFunctions'>, 'test_add')
>>> suite.cases[0][1]
'test_add'
>>> suite.cases.__getitem__(0).__getitem__(1)
'test_add'
>>> 
>>> suite[0]
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    suite[0]
TypeError: 'TestSuite' object does not support indexing
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
>>> len(suite)
2
>>> suite[0]
'test_add'
>>> suite[1]
'test_sub'
>>> suite[2]
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    suite[2]
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 77, in __getitem__
    return self.cases[index][1]
IndexError: list index out of range
>>> 
>>> suite
<beck.TestSuite object at 0x10380f8d0>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 61, in <module>
    assert repr(suite) == "TestSuite('test_add', 'test_sub')"
AssertionError
>>> repr(TestSuite)
"<class 'beck.TestSuite'>"
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 61, in <module>
    assert repr(suite) == "TestSuite('test_add', 'test_sub')"
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 80, in __repr__
    return f'TestSuite{casenames}'
NameError: name 'casenames' is not defined
>>> 
>>> list(suite)
['test_add', 'test_sub']
>>> suite[0]
'test_add'
>>> suite[1]
'test_sub'
>>> tuple(suite)
('test_add', 'test_sub')
>>> set(suite)
{'test_add', 'test_sub'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
>>> 
>>> 
>>> 
>>> suite
TestSuite('test_add', 'test_sub')
>>> print(suite)
TestSuite('test_add', 'test_sub')
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # The __str__ is used by print() as a first choice, which falls back to __repr__ if there is not __str__
>>> # The reason there is both a __str__ and __repr__ is that we have two diffent users:
>>> #     End-users expect pretty output
>>> #     Programmers need informative output
>>> # That said, sometime the pretty way is sufficiently informative and both are the same
>>> 
>>> 
>>> repr(30)
'30'
>>> str(30)
'30'
>>> 30
30
>>> print(30)
30
>>> 
>>> s = '70'
>>> print(s)
70
>>> s
'70'
>>> sub(70, 30)
40
>>> sub(70, 'hello')
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    sub(70, 'hello')
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 10, in sub
    return x - y            # <== Intentionally correct code
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..
2 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
...
3 run, 1 failed
>>> suite
TestSuite('test_add', 'test_sub', 'test_sub_bad_args')
>>> len(suite)
3
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..ERROR:root:Test failed: test_sub_bad_args
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 25, in test_sub_bad_args
    assert False
AssertionError
.
3 run, 2 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
...
3 run, 1 failed
>>> 
>>> assert 3 + 5 == 8
>>> assert 3 + 5 == 10
Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    assert 3 + 5 == 10
AssertionError
>>> assert 32 / 0 == 5
Traceback (most recent call last):
  File "<pyshell#323>", line 1, in <module>
    assert 32 / 0 == 5
ZeroDivisionError: division by zero
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 67, in <module>
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 69, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 21, in test_sub_bad_args
    with self.assert_raises(TypeError):
AttributeError: 'TestMathFunctions' object has no attribute 'assert_raises'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 67, in <module>
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 72, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 21, in test_sub_bad_args
    with self.assert_raises(TypeError):
TypeError: assert_raises() takes 1 positional argument but 2 were given
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
..Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 67, in <module>
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 72, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 45, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 21, in test_sub_bad_args
    with self.assert_raises(TypeError):
AttributeError: __enter__
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> with Raises(TypeError):
	30 + 40

	
70
Traceback (most recent call last):
  File "<pyshell#325>", line 2, in <module>
    30 + 40
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 38, in __exit__
    assert False, f'Expected {self.exception}'
AssertionError: Expected <class 'TypeError'>
>>> with Raises(TypeError):
	raise RuntimeError

Traceback (most recent call last):
  File "<pyshell#327>", line 2, in <module>
    raise RuntimeError
RuntimeError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#327>", line 2, in <module>
    raise RuntimeError
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 38, in __exit__
    assert False, f'Expected {self.exception}'
AssertionError: Expected <class 'TypeError'>
>>> with Raises(TypeError):
	raise TypeError

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 57, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 57, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
...
3 run, 1 failed
>>> e = KeyError('susan')
>>> e
KeyError('susan',)
>>> e.args
('susan',)
>>> 
>>> 
>>> str.__getitem__ = None
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    str.__getitem__ = None
TypeError: can't set attributes of built-in/extension type 'str'
>>> 
>>> class MyStr(str):
	def __getitem__(self, index):
		return self[index * 2]

	
>>> s = MyStr('the tale of two cities')
>>> s.upper()
'THE TALE OF TWO CITIES'
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    s[1]
  File "<pyshell#340>", line 3, in __getitem__
    return self[index * 2]
  File "<pyshell#340>", line 3, in __getitem__
    return self[index * 2]
  File "<pyshell#340>", line 3, in __getitem__
    return self[index * 2]
  [Previous line repeated 327 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> class MyStr(str):
	def __getitem__(self, index):
		return str.__getitem__(self, index * 2)

	
>>> s = MyStr('the tale of two cities')
>>> s.upper()
'THE TALE OF TWO CITIES'
>>> s[1]
'e'
>>> s[2]
't'
>>> len(s)
22
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
...
3 run, 1 failed
>>> len(suite)
3
>>> suite
TestSuite('test_add', 'test_sub', 'test_sub_bad_args')
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_beck.py =========
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
Done!
ERROR:root:Test failed: test_add
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 15, in test_add
    assert add(3, 5) == 8
AssertionError
...
3 run, 1 failed
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_beck.py", line 66, in <module>
    assert repr(suite) == "TestSuite('test_add', 'test_sub', 'test_sub_bad_args')"
AssertionError
>>> suite
<beck.TestSuite object at 0x1042d2940>
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> # 3:15
>>> 
>>> 
>>> def fib(n):
	if n < 2:
		return 1
	return fib(n-1) + fib(n-2)

>>> fib(1)
1
>>> fib(2)
2
>>> fib(3)
3
>>> fib(4)
5
>>> fib(5)
8
>>> fib(6)
13
>>> # Little Schemer
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> import requests
>>> r = requests('https://chart.googleapis.com/chart', params=dict(cht='qr', chs='300x300', chl='Hello World'))
Traceback (most recent call last):
  File "<pyshell#370>", line 1, in <module>
    r = requests('https://chart.googleapis.com/chart', params=dict(cht='qr', chs='300x300', chl='Hello World'))
TypeError: 'module' object is not callable
>>> r = requests.get('https://chart.googleapis.com/chart', params=dict(cht='qr', chs='300x300', chl='Hello World'))
>>> r.status_code
200
>>> image = r.content
>>> type(image)
<class 'bytes'>
>>> 
>>> 
>>> 
>>> import requests
>>> r = requests('https://chart.googleapis.com/chart', params=dict(cht='qr', chs='300x300', chl='Hello World'))
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    r = requests('https://chart.googleapis.com/chart', params=dict(cht='qr', chs='300x300', chl='Hello World'))
TypeError: 'module' object is not callable
>>> 
>>> 



>>> 


>>> 



>>> 



>>> 



>>> import requests
>>> r = requests.get('https://chart.googleapis.com/chart', params=dict(cht='qr', chs='300x300', chl='Hello World'))
>>> image = r.content
>>> r.url
'https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=Hello+World'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> 
>>> 
>>> 
>>> chr(65)
'A'
>>> chr(97)
'a'
>>> ord('a')
97
>>> ord('e')
101
>>> ord(b'e')
101
>>> 
>>> 
>>> [ord(c) for c in 'Raymond']
[82, 97, 121, 109, 111, 110, 100]
>>> list(map(ord, 'Raymond'))
[82, 97, 121, 109, 111, 110, 100]
>>> len(image)
2826
>>> [ord(c) for c in image[:8]]
Traceback (most recent call last):
  File "<pyshell#403>", line 1, in <module>
    [ord(c) for c in image[:8]]
  File "<pyshell#403>", line 1, in <listcomp>
    [ord(c) for c in image[:8]]
TypeError: ord() expected string of length 1, but int found
>>> list(image[:8])
[137, 80, 78, 71, 13, 10, 26, 10]
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> r.url
'https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=BEGIN%3AVCARD%0AVERSION%3A2.1%0AN%3ASchmidt%3BGertrude%0AFN%3AGertrude+Schmidt%0AORG%3ARaisins+R+Us%2C+Inc.%0ATITLE%3AVP+Business+Development%0ATEL%3BWORK%3BVOICE%3A559-555-6700%0AADR%3BWORK%3BPREF%3A%3B%3B100+Flat+Grape+Dr.%3BFresno%3BCA%3B95551%3BUnited+States+of+America%0AEMAIL%3Agertrude%40example.com%0AREV%3A20170424T195243Z%0AEND%3AVCARD%0A'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: raymond_at_example_dot_com.png
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.png
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.png
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.png
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.png
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.png
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.png
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.png
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.png
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.png
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.png
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.png
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.png
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: "raymond_at_example_dot_com".vcf
INFO:root:Wrote: "raymond_at_example_dot_com".png
INFO:root:Wrote: "mary_at_example_dot_com".vcf
INFO:root:Wrote: "mary_at_example_dot_com".png
INFO:root:Wrote: "harold_at_example_dot_com".vcf
INFO:root:Wrote: "harold_at_example_dot_com".png
INFO:root:Wrote: "martin_at_example_dot_com".vcf
INFO:root:Wrote: "martin_at_example_dot_com".png
INFO:root:Wrote: "david_at_example_dot_com".vcf
INFO:root:Wrote: "david_at_example_dot_com".png
INFO:root:Wrote: "luis_at_example_dot_com".vcf
INFO:root:Wrote: "luis_at_example_dot_com".png
INFO:root:Wrote: "fritz_at_example_dot_com".vcf
INFO:root:Wrote: "fritz_at_example_dot_com".png
INFO:root:Wrote: "esmerelda_at_example_dot_com".vcf
INFO:root:Wrote: "esmerelda_at_example_dot_com".png
INFO:root:Wrote: "marilyn_at_example_dot_com".vcf
INFO:root:Wrote: "marilyn_at_example_dot_com".png
INFO:root:Wrote: "blair_at_example_dot_com".vcf
INFO:root:Wrote: "blair_at_example_dot_com".png
INFO:root:Wrote: "djones_at_example_dot_com".vcf
INFO:root:Wrote: "djones_at_example_dot_com".png
INFO:root:Wrote: "hdavis_at_example_dot_com".vcf
INFO:root:Wrote: "hdavis_at_example_dot_com".png
INFO:root:Wrote: "gertrude_at_example_dot_com".vcf
INFO:root:Wrote: "gertrude_at_example_dot_com".png
>>> print(vcard)
BEGIN:VCARD
VERSION:2.1
N:"Schmidt";"Gertrude"
FN:"Gertrude" "Schmidt"
ORG:Raisins R Us, Inc.
TITLE:"VP Business Development"
TEL;WORK;VOICE:"559-555-6700"
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:"gertrude@example.com"
REV:20170424T195243Z
END:VCARD

>>> email
'"gertrude@example.com"'
>>> line
'"Schmidt","Gertrude","VP Business Development","gertrude@example.com","559-555-6700"'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: raymond_at_example_dot_com.png
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.png
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.png
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.png
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.png
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.png
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.png
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.png
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.png
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.png
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.png
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.png
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.png
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
INFO:root:Wrote: raymond_at_example_dot_com.vcf
INFO:root:Wrote: raymond_at_example_dot_com.png
INFO:root:Wrote: mary_at_example_dot_com.vcf
INFO:root:Wrote: mary_at_example_dot_com.png
INFO:root:Wrote: harold_at_example_dot_com.vcf
INFO:root:Wrote: harold_at_example_dot_com.png
INFO:root:Wrote: martin_at_example_dot_com.vcf
INFO:root:Wrote: martin_at_example_dot_com.png
INFO:root:Wrote: david_at_example_dot_com.vcf
INFO:root:Wrote: david_at_example_dot_com.png
INFO:root:Wrote: luis_at_example_dot_com.vcf
INFO:root:Wrote: luis_at_example_dot_com.png
INFO:root:Wrote: fritz_at_example_dot_com.vcf
INFO:root:Wrote: fritz_at_example_dot_com.png
INFO:root:Wrote: esmerelda_at_example_dot_com.vcf
INFO:root:Wrote: esmerelda_at_example_dot_com.png
INFO:root:Wrote: marilyn_at_example_dot_com.vcf
INFO:root:Wrote: marilyn_at_example_dot_com.png
INFO:root:Wrote: blair_at_example_dot_com.vcf
INFO:root:Wrote: blair_at_example_dot_com.png
INFO:root:Wrote: djones_at_example_dot_com.vcf
INFO:root:Wrote: djones_at_example_dot_com.png
INFO:root:Wrote: hdavis_at_example_dot_com.vcf
INFO:root:Wrote: hdavis_at_example_dot_com.png
INFO:root:Wrote: gertrude_at_example_dot_com.vcf
INFO:root:Wrote: gertrude_at_example_dot_com.png
>>> import vcard
>>> print(vcard.make_vcard('Navra', 'Ananda', 'Manager', 'navra@cisco.com', '555-1212'))
BEGIN:VCARD
VERSION:2.1
N:Ananda;Navra
FN:Navra Ananda
ORG:Raisins R Us, Inc.
TITLE:Manager
TEL;WORK;VOICE:555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:navra@cisco.com
REV:20170424T195243Z
END:VCARD

>>> image = vcard.make_qr_code('Cisco Rocks!')
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
>>> 30 + 40
70
>>> 30 +
SyntaxError: invalid syntax
>>> 30 + \
      40
70
>>> # ( )   [ ]   { }
>>> (30 +
     40)
70
>>> names = [
	'Raymond Hettinger',
	'Rachel Hettinger
	
SyntaxError: EOL while scanning string literal
>>> names = [
	'Raymond Hettinger',
	'Rachel Hettinger'
]
>>> names
['Raymond Hettinger', 'Rachel Hettinger']
>>> 
>>> 
>>> names = [
	'Raymond Hettinger',
	'Rachel Hettinger',
	'Matthew Hettinger'
]
>>> 
>>> names
['Raymond Hettinger', 'Rachel Hettinger', 'Matthew Hettinger']
>>> names = [
	'Raymond Hettinger',
	'Rachel Hettinger'
	'Matthew Hettinger'
]
>>> names
['Raymond Hettinger', 'Rachel HettingerMatthew Hettinger']
>>> #   - 'Rachel Hettinger'
>>> #   + 'Rachel Hettinger',
>>> #   + 'Matthew Hettinger'
>>> names = [
	'Raymond Hettinger',
	'Rachel Hettinger',
]
>>> names
['Raymond Hettinger', 'Rachel Hettinger']
>>> names = [
	'Raymond Hettinger',
	'Rachel Hettinger',
	'Matthew Hettinger',
]
>>> #   + 'Matthew Hettinger,'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj164/vcard.py ===========
>>> 
>>> 
>>> 
>>> 
>>> n = 10
>>> desks = [[] for i in range(n)]
>>> desks
[[], [], [], [], [], [], [], [], [], []]
>>> folders = [[] for i in range(n)]
>>> folders
[[], [], [], [], [], [], [], [], [], []]
>>> 
>>> 
>>> n = 10
>>> desks = [[] for i in range(n)]
>>> folders = [[] for i in range(n)]
>>> 
>>> n
10
>>> desks
[[], [], [], [], [], [], [], [], [], []]
>>> folders
[[], [], [], [], [], [], [], [], [], []]
>>> name = 'tony'
>>> color = 'orange'
>>> phone = 5250108
>>> i = phone % 10
>>> i
8
>>> desks[i].append(name)
>>> folders[i].append(color)
>>> 
>>> desks
[[], [], [], [], [], [], [], [], ['tony'], []]
>>> folders
[[], [], [], [], [], [], [], [], ['orange'], []]
>>> name = 'alejandro'
>>> color = 'blue'
>>> phone = 5254536
>>> i = phone % 10
>>> desks[i].append(name)
>>> folders[i].append(color)
>>> 
>>> desks
[[], [], [], [], [], [], ['alejandro'], [], ['tony'], []]
>>> folders
[[], [], [], [], [], [], ['blue'], [], ['orange'], []]
>>> name = 'philip'
>>> color = 'white'
>>> phone = 5254278
>>> i = phone % 10
>>> desks[i].append(name)
>>> folders[i].append(color)
>>> 
>>> desks
[[], [], [], [], [], [], ['alejandro'], [], ['tony', 'philip'], []]
>>> folders
[[], [], [], [], [], [], ['blue'], [], ['orange', 'white'], []]
>>> 
>>> name = 'rama'
>>> color = 'white'
>>> phone = 8534008
>>> i = phone % 10
>>> desks[i].append(name)
>>> folders[i].append(color)
>>> 
>>> desks
[[], [], [], [], [], [], ['alejandro'], [], ['tony', 'philip', 'rama'], []]
>>> folders
[[], [], [], [], [], [], ['blue'], [], ['orange', 'white', 'white'], []]
>>> 
>>> name = 'rucha'
>>> color = 'green'
>>> phone = 8532507
>>> i = phone % 10
>>> desks[i].append(name)
>>> folders[i].append(color)
>>> 
>>> desks
[[], [], [], [], [], [], ['alejandro'], ['rucha'], ['tony', 'philip', 'rama'], []]
>>> folders
[[], [], [], [], [], [], ['blue'], ['green'], ['orange', 'white', 'white'], []]
>>> 
>>> name = 'alejandro'
>>> phone = 5254536
>>> i = phone % 10
>>> j = desks[i].index(name)
>>> j
0
>>> folders[i][j]
'blue'
>>> 
>>> name = 'philip'
>>> phone = 5254278
>>> i = phone % 10
>>> j = desks[i].index(name)
>>> folders[i][j]
'white'
>>> (1 + 1 + 1 + 2 + 3) / 5
1.6
>>> phone = 5254536
>>> phone % 8
0
>>> phone & 7
0
>>> phone = 8532507
>>> phone % 8
3
>>> phone & 7
3
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 'raymond'.__hash__()
4238312204208759129
>>> abs('raymond'.__hash__())
4238312204208759129
>>> 
>>> 
>>> 
>>> def myhash(s):
	h = 0
	for c in s:
		h += ord(c)
	return h

>>> myhash('raymond')
762
>>> [ord(c) for c in 'raymond']
[114, 97, 121, 109, 111, 110, 100]
>>> sum([ord(c) for c in 'raymond'])
762
>>> myhash('arymond')
762
>>> def myhash(s):
	h = 0
	for c in s:
		h += ord(c) * 17
	return h

>>> myhash('raymond')
12954
>>> myhash('arymond')
12954
>>> def myhash(s):
	h = 0
	for c in s:
		h = h * 17 + ord(c)
	return h

>>> myhash('raymond')
2900084602
>>> myhash('arymond')
2513883498
>>> myhash('raymond')
2900084602
>>> myhash('rachel')
170483503
>>> 
=============================== RESTART: Shell ===============================
>>> def myhash(s):
	h = 0
	for c in s:
		h = h * 17 + ord(c)
	return h

>>> myhash('rachel')
170483503
>>> import random
>>> import time
>>> random.seed(int(time.time()))
>>> random.range(1000000)
Traceback (most recent call last):
  File "<pyshell#558>", line 1, in <module>
    random.range(1000000)
AttributeError: module 'random' has no attribute 'range'
>>> random.randrange(1000000)
902537
>>> random.seed(int(time.time()))
>>> random.randrange(1000000)
894405
>>> def myhash(s):
	h = 0
	for c in s:
		h = h * 17 + ord(c)
	return h

>>> hashseed = random.randrange(1000000)
>>> def myhash(s):
	h = hashseed
	for c in s:
		h = h * 17 + ord(c)
	return h

>>> myhash('raymond')
278510836593873
>>> myhash('rachel')
16382990278166
>>> myhash('raymond')
278510836593873
>>> 
=============================== RESTART: Shell ===============================
>>> import time
>>> import random
>>> random.seed(int(time.time()))
>>> hashseed = random.randrange(1000000)
>>> def myhash(s):
	h = hashseed
	for c in s:
		h = h * 17 + ord(c)
	return h

>>> myhash('raymond')
362494032119437
>>> myhash('rachel')
21323178250258
>>> myhash('raymond')
362494032119437
>>> time.time()
1499904497.9022238
>>> int(time.time())
1499904501
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========

0 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========

0 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 11, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 7, in test_basics
    d = Dict()
NameError: name 'Dict' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 2, in <module>
    from dictionary import Dict
ImportError: cannot import name 'Dict'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.
1 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 15, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 8, in test_basics
    d['philip'] = 'white'
TypeError: 'Dict' object does not support item assignment
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.
1 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.
1 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 15, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 8, in test_basics
    d['philip'] = 'white'
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 7, in __setitem__
    h = myhash(key)
NameError: name 'myhash' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 22, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 8, in test_basics
    d['philip'] = 'white'
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 7, in __setitem__
    h = myhash(key)
NameError: name 'myhash' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 22, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 8, in test_basics
    d['philip'] = 'white'
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 10, in __setitem__
    h = myhash(key)
TypeError: myhash() takes 0 positional arguments but 1 was given
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 22, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 14, in test_myhash
    assert isinstance(myhash('raymond'), int)
NameError: name 'myhash' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_myhash
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 14, in test_myhash
    assert isinstance(myhash('raymond'), int)
AssertionError
.
2 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_myhash
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 17, in test_myhash
    assert myhash('raymond') != myhash('rachel')
AssertionError
.
2 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 2, in <module>
    from dictionary import Dict, myhash
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 6
    h = h * 17 + ord(c)
                      ^
TabError: inconsistent use of tabs and spaces in indentation
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..
2 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 22, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 8, in test_basics
    d['philip'] = 'white'
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 14, in __setitem__
    i = h % len(self.desks)
AttributeError: 'Dict' object has no attribute 'desks'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 22, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 8, in test_basics
    d['philip'] = 'white'
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 19, in __setitem__
    i = h % len(self.n)
TypeError: object of type 'int' has no len()
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..
2 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..
2 run, 0 failed
>>> d = Dict()
>>> d['raymond'] = 'red'
>>> d['rachel'] = 'blue'
>>> d['matthew'] = 'yellow'
>>> 
>>> d.n
8
>>> d.desks
[[], [], ['raymond', 'matthew'], [], [], [], [], ['rachel']]
>>> d.folders
[[], [], ['red', 'yellow'], [], [], [], [], ['blue']]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..
2 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..
2 run, 0 failed
>>> hash('raymond')
-5395593237814872907
>>> 

>>> 
