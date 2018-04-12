Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/log_parse_demo.py =======
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/log_parse_demo.py =======
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/log_parse_demo.py", line 5, in <module>
    visited = collections.Counter()
NameError: name 'collections' is not defined
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj164/log_parse_demo.py =======
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/log_parse_demo.py", line 5, in <module>
    visited = colleckions.Counter()
NameError: name 'colleckions' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 5, in <module>
    assert square(3) == 9
NameError: name 'square' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 8, in <module>
    assert square(3) == 9
TypeError: square() takes 0 positional arguments but 1 was given
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 8, in <module>
    assert square(3) == 9
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 9, in <module>
    assert square(4) == 16
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 13, in <module>
    assert cube(11) == 1331
NameError: name 'cube' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 14, in <module>
    assert cube(11) == 1331
TypeError: cube() takes 0 positional arguments but 1 was given
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 14, in <module>
    assert cube(11) == 1331
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 15, in <module>
    assert cube(5) == 125
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
>>> 27 + 9 + 7
43
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 8, in <module>
    assert f(x=3, n=4) == 43
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 9, in <module>
    assert f(x=3, n=4) == 43
  File "/Users/raymond/Dropbox/Public/sj164/tmp.py", line 7, in f
    return cube(x) + square(x) + nth_prime(n)
NameError: name 'cube' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/tmp.py ============
>>> # High level Python
>>> # High level TTD concepts
>>> # Python basics
>>> # Build a small test framework
>>> #   unittest doctest nose py.test coverage  hypothesis  itertool   logging  -> PyATS
>>> 
>>> 
>>> # types of testing
>>> # install
>>> 
>>> 
>>> # http://bit.ly/py-install36          

>>> import bottle
>>> import hypothesis
>>> 
>>> 
>>> 30 + 40
70
>>> import sys
>>> sys.stdout
<idlelib.run.PseudoOutputFile object at 0x1034c4f60>
>>> print(30 + 40)
70
>>> print(30 + 40, 11 + 22)
70 33
>>> print(30 + 40, 11 + 22, file=sys.stderr)
70 33
>>> 
>>> 
>>> 



>>> import sys
>>> print(30 + 40, 11 + 22)
70 33
>>> print(30 + 40, 11 + 22, file=sys.stderr)
70 33
>>> print(30 + 40, 11 + 22, file=sys.stderr, sep='~')
70~33
>>> print(30 + 40, 11 + 22, sep='~', file=sys.stderr)
70~33
>>> import collections
>>> import re
>>> print(30 + 40, 11 + 22, sep='~', file=sys.stdout)
70~33
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/welcome.py ==========
>>> __doc__                 # dunder doc
'A good start'
>>> 30 + 40
70
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/welcome.py ==========
 Hey, hey!  It moves
  Hey, hey!  It moves
   Hey, hey!  It moves
    Hey, hey!  It moves
     Hey, hey!  It moves
      Hey, hey!  It moves
       Hey, hey!  It moves
        Hey, hey!  It moves
         Hey, hey!  It moves
          Hey, hey!  It moves
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/welcome.py ==========
 Hey, hey!  It moves
  Hey, hey!  It moves
   Hey, hey!  It moves
    Hey, hey!  It moves
     Hey, hey!  It moves
      Hey, hey!  It moves
       Hey, hey!  It moves
        Hey, hey!  It moves
         Hey, hey!  It moves
          Hey, hey!  It moves
 Hey, hey!  It moves
  Hey, hey!  It moves
   Hey, hey!  It moves
    Hey, hey!  It moves
     Hey, hey!  It moves
      Hey, hey!  It moves
       Hey, hey!  It moves
        Hey, hey!  It moves
         Hey, hey!  It moves
          Hey, hey!  It moves
>>> # http://bit.ly/python-sj164
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/welcome.py ==========
 Hey, hey!  It moves
  Hey, hey!  It moves
   Hey, hey!  It moves
    Hey, hey!  It moves
     Hey, hey!  It moves
      Hey, hey!  It moves
       Hey, hey!  It moves
        Hey, hey!  It moves
         Hey, hey!  It moves
          Hey, hey!  It moves
 Howdy!
  Howdy!
   Howdy!
    Howdy!
     Howdy!
      Howdy!
       Howdy!
        Howdy!
         Howdy!
          Howdy!
>>> print('My scratch sheet and output window')
My scratch sheet and output window
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/download.py ==========
======================== Source: https://dl.dropboxusercontent.com/u/3967849/sj164/links.txt ========================
                                    Starting download at Mon Jul 10 13:52:03 2017                                    
200* OK               https://dl.dropbox.com/u/3967849/shared/call_by_object.txt --> notes/call_by_object.txt  (current) 
200* OK               https://dl.dropbox.com/u/3967849/sj164/links.txt        --> notes/links.txt           (current) 
200  OK               https://dl.dropbox.com/u/3967849/sj164/log_parse_demo.py --> notes/log_parse_demo.py   (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/picirc.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/banner.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/norvig_corrector.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/corpus.dat
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/highlight.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/publish.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/purpose.jpg
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/picirc.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/congress_data.zip
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/PythonAwesome.pdf
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/islands.pdf
200  OK               https://dl.dropbox.com/u/3967849/sj164/day1.py          --> notes/day1.py             (updated) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/__init__.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/bottle.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/CSRRESTAPI.pdf
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/Raymond_Hettinger.png
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/Raymond_Hettinger.vcf
200* OK               https://dl.dropbox.com/u/3967849/shared/books.json      --> notes/books.json          (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/books.xml       --> notes/books.xml           (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/crossword_challenge.py
200* OK               https://dl.dropbox.com/u/3967849/shared/dns_servers.json --> notes/dns_servers.json    (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/email.txt       --> notes/email.txt           (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/english_composition.txt --> notes/english_composition.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/family_template.txt --> notes/family_template.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/fruit.xml       --> notes/fruit.xml           (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/hamlet.txt      --> notes/hamlet.txt          (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/interfaces.xml  --> notes/interfaces.xml      (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/ipv4_int_bri.txt --> notes/ipv4_int_bri.txt    (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/kap.dot
200* OK               https://dl.dropbox.com/u/3967849/shared/kap.svg         --> notes/kap.svg             (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/member_template.txt --> notes/member_template.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/nasa_19950801.log --> notes/nasa_19950801.log   (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/oop_story.txt   --> notes/oop_story.txt       (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/parse_demo2.txt --> notes/parse_demo2.txt     (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/ping_output.txt --> notes/ping_output.txt     (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/queue_stats.txt --> notes/queue_stats.txt     (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/raisin_team.csv --> notes/raisin_team.csv     (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/raisin_team_update.csv --> notes/raisin_team_update.csv (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/re.txt          --> notes/re.txt              (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/rss.xml         --> notes/rss.xml             (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/show_controllers.txt --> notes/show_controllers.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/stocks.txt      --> notes/stocks.txt          (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/team_history.json --> notes/team_history.json   (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/team_history.txt --> notes/team_history.txt    (current) 
>>> # http://bit.ly/python-sj164
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/download.py ==========
======================== Source: https://dl.dropboxusercontent.com/u/3967849/sj164/links.txt ========================
                                    Starting download at Mon Jul 10 13:55:02 2017                                    
200* OK               https://dl.dropbox.com/u/3967849/shared/call_by_object.txt --> notestdd/call_by_object.txt (updated) 
200* OK               https://dl.dropbox.com/u/3967849/sj164/links.txt        --> notestdd/links.txt        (updated) 
200  OK               https://dl.dropbox.com/u/3967849/sj164/log_parse_demo.py --> notestdd/log_parse_demo.py (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/picirc.py       --> notestdd/picirc.py        (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/banner.py       --> notestdd/banner.py        (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/norvig_corrector.py --> notestdd/norvig_corrector.py (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/corpus.dat      --> notestdd/corpus.dat       (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/highlight.py    --> notestdd/highlight.py     (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/publish.py      --> notestdd/publish.py       (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/purpose.jpg     --> notestdd/purpose.jpg      (updated) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/picirc.py
200  OK               https://dl.dropbox.com/u/3967849/shared/congress_data.zip --> notestdd/congress_data.zip (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/PythonAwesome.pdf --> notestdd/PythonAwesome.pdf (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/islands.pdf     --> notestdd/islands.pdf      (updated) 
200  OK               https://dl.dropbox.com/u/3967849/sj164/day1.py          --> notestdd/day1.py          (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/__init__.py     --> notestdd/__init__.py      (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/bottle.py       --> notestdd/bottle.py        (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/CSRRESTAPI.pdf  --> notestdd/CSRRESTAPI.pdf   (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/Raymond_Hettinger.png --> notestdd/Raymond_Hettinger.png (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/Raymond_Hettinger.vcf --> notestdd/Raymond_Hettinger.vcf (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/books.json      --> notestdd/books.json       (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/books.xml       --> notestdd/books.xml        (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/crossword_challenge.py --> notestdd/crossword_challenge.py (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/dns_servers.json --> notestdd/dns_servers.json (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/email.txt       --> notestdd/email.txt        (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/english_composition.txt --> notestdd/english_composition.txt (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/family_template.txt --> notestdd/family_template.txt (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/fruit.xml       --> notestdd/fruit.xml        (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/hamlet.txt      --> notestdd/hamlet.txt       (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/interfaces.xml  --> notestdd/interfaces.xml   (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/ipv4_int_bri.txt --> notestdd/ipv4_int_bri.txt (updated) 
200  OK               https://dl.dropbox.com/u/3967849/shared/kap.dot         --> notestdd/kap.dot          (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/kap.svg         --> notestdd/kap.svg          (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/member_template.txt --> notestdd/member_template.txt (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/nasa_19950801.log --> notestdd/nasa_19950801.log (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/oop_story.txt   --> notestdd/oop_story.txt    (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/parse_demo2.txt --> notestdd/parse_demo2.txt  (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/ping_output.txt --> notestdd/ping_output.txt  (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/queue_stats.txt --> notestdd/queue_stats.txt  (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/raisin_team.csv --> notestdd/raisin_team.csv  (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/raisin_team_update.csv --> notestdd/raisin_team_update.csv (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/re.txt          --> notestdd/re.txt           (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/rss.xml         --> notestdd/rss.xml          (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/show_controllers.txt --> notestdd/show_controllers.txt (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/stocks.txt      --> notestdd/stocks.txt       (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/team_history.json --> notestdd/team_history.json (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/team_history.txt --> notestdd/team_history.txt (updated) 
>>> 
>>> 
>>> 
>>> with open('notestdd/hamlet.txt') as f:
	print(len(f.read()))

	
194355
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_mininum.py ========
>>> print(__doc__)
 The minimum you need to follow the great Kent Beck
    and his magical example of teaching Python, and TDD,
    to build a unittest framework from scratch while
    using it.  Sounds crazy.

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_mininum.py ========
>>> 35 / 2
17.5
>>> 35 // 2
17
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_mininum.py ========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_mininum.py ========
>>> collatz(10)
5
>>> collatz(11)
34
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_mininum.py ========
>>> help(collatz)
Help on function collatz in module __main__:

collatz(x)
    Famous function in computer science
    for the Collatz conjecture which is
    the simplest known example of Halting Problem.
    
    
    >>> collatz(10)
    5
    >>> collatz(11)
    34

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_mininum.py ========
Run directly
>>> import the_minimum
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    import the_minimum
ModuleNotFoundError: No module named 'the_minimum'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
Run directly
>>> import the_minimum
>>> the_minimum.collatz(20)
10
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 14, in __main__.collatz
Failed example:
    collatz(11)
Expected:
    34
Got:
    23
**********************************************************************
1 items had failures:
   1 of   2 in __main__.collatz
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
=============================== RESTART: Shell ===============================
>>> import the_minimum
>>> the_minimum.__name__
'the_minimum'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 12, in __main__.collatz
Failed example:
    collatz(10)  
Expected:
    5  
Got:
    5
**********************************************************************
1 items had failures:
   1 of   2 in __main__.collatz
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> collatz(-5)
-14
>>> collatz(5.5)
17.5
>>> collatz('hello')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    collatz('hello')
  File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 18, in collatz
    if x % 2 == 0:
TypeError: not all arguments converted during string formatting
>>> collatz(5, 2)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    collatz(5, 2)
TypeError: collatz() takes 1 positional argument but 2 were given
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> Employee
<class '__main__.Employee'>
>>> vikas
<__main__.Employee object at 0x1033d7cc0>
>>> craig
<__main__.Employee object at 0x1033d7ac8>
>>> rucha
<__main__.Employee object at 0x1034bf630>
>>> 
>>> 
>>> vikas.__class__
<class '__main__.Employee'>
>>> type(vikas)
<class '__main__.Employee'>
>>> vikas.__dict__
{}
>>> vars(vikas)
{}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> navra
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    navra
NameError: name 'navra' is not defined
>>> 
>>> 
>>> # variable ==> attribute
>>> # function ==> method
>>> 
>>> 
>>> vikas.gender
'male'
>>> vikas.country
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    vikas.country
AttributeError: 'Employee' object has no attribute 'country'
>>> vikas.name = 'Vikas Kokkalia'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
>>> 
>>> type(vikas)
<class '__main__.Employee'>
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male'}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> Employee.company
'Cisco'
>>> vikas.company
'Cisco'
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male'}
>>> 
>>> 
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male'}
>>> type(vikas)
<class '__main__.Employee'>
>>> vars(type(vikas))
mappingproxy({'__module__': '__main__', '__doc__': 'Worker at a company', 'company': 'Cisco', '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>})
>>> 
>>> 
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male'}
>>> vars(rucha)
{'name': 'Rucha Gupte', 'gender': 'female'}
>>> vars(craig)
{'name': 'Craig Williams', 'gender': 'male'}
>>> 
>>> 
>>> vars(craig)
{'name': 'Craig Williams', 'gender': 'male'}
>>> type(craig)
<class '__main__.Employee'>
>>> craig.gender
'male'
>>> craig.company
'Cisco'
>>> 
>>> 
>>> # English
>>> # Action
>>> # V DO
>>> # run('dog')
>>> # jump('cat')
>>> 
>>> # German
>>> # Thing
>>> # N V
>>> # dog run
>>> # cat jump
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> craig.gender
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    craig.gender
AttributeError: 'Employee' object has no attribute 'gender'
>>> vars(craig)
{}
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male'}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> Employee()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    Employee()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'gender'
>>> 
>>> 
>>> # The name __init__ is a special name hardwired into Python
>>> # If the __init__ method exists, it is automatically
>>> # called when the instance is created.
>>> 
>>> # This is great design.
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 34, in <module>
    vikas = Employee('Vikas Kokkalla', 'male', 35)
  File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 32, in __init__
    this.salary
AttributeError: 'Employee' object has no attribute 'salary'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
>>> rucha.salary
39
>>> give_raise(rucha, 20)
>>> rucha.salary
46.8
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 42, in <module>
    print(rucha.salar)
AttributeError: 'Employee' object has no attribute 'salar'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
46.8
TestResults(failed=0, attempted=2)
>>> 
>>> 
>>> dir(craig)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'company', 'gender', 'give_raise', 'name', 'salary']
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
46.8
TestResults(failed=0, attempted=2)
>>> 
>>> 
>>> rucha.salary
46.8
>>> rucha.company
'Cisco'
>>> rucha.x
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    rucha.x
AttributeError: 'Employee' object has no attribute 'x'
>>> 
>>> 
>>> k = 'company'
>>> rucha.k
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    rucha.k
AttributeError: 'Employee' object has no attribute 'k'
>>> 
>>> 
>>> getattr(rucha, k)
'Cisco'
>>> k = 'salary'
>>> getattr(rucha, k)
46.8
>>> for attr in ['salary', 'name', 'gender']:
	print(attr, getattr(craig, attr))

	
salary 31
name Craig Williams
gender male
>>> craig.attr
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    craig.attr
AttributeError: 'Employee' object has no attribute 'attr'
>>> craig.salary
31
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
46.8
male
male
TestResults(failed=0, attempted=2)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46.8
male
male
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46.8
male
male
>>> Unemployed.company
'None'
>>> Employee.company
'Cisco'
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46.8
male
male
>>> Unemployed.company
'None'
>>> Employee.company
'Cisco'
>>> Unemployed.status
'Alive'
>>> Employee.status
'Alive'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46.8
male
male
>>> Unemployed.company
'None'
>>> Employee.company
'Cisco'
>>> Unemployed.status
'Alive'
>>> Employee.status
'Alive'
>>> 
>>> 
>>> 
>>> vars(vikas)
{'name': 'Vikas Kokkalla', 'gender': 'male', 'salary': 35}
>>> type(vikas)
<class '__main__.Employee'>
>>> vars(type(vikas))
mappingproxy({'__module__': '__main__', '__doc__': 'Worker at a company', 'company': 'Cisco', '__init__': <function Employee.__init__ at 0x1036c2840>, 'give_raise': <function Employee.give_raise at 0x1036c28c8>})
>>> Employee.__bases__
(<class '__main__.LivingThing'>,)
>>> vars(LivingThing)
mappingproxy({'__module__': '__main__', 'status': 'Alive', '__dict__': <attribute '__dict__' of 'LivingThing' objects>, '__weakref__': <attribute '__weakref__' of 'LivingThing' objects>, '__doc__': None})
>>> 
>>> vikas.gender
'male'
>>> vikas.company
'Cisco'
>>> vikas.status
'Alive'
>>> vikas.xyz
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    vikas.xyz
AttributeError: 'Employee' object has no attribute 'xyz'
>>> 
>>> 
>>> 
>>> 
>>> # inst.a:   vars(inst) -> vars(class) -> vars(base) -> AttributeError
>>> #             unique    shared by insts   shared by classes
>>> 
>>> 
>>> # base class   ==   parent class == superclass
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.
----------------------------------------------------------------------
Ran 1 test in 0.026s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.
----------------------------------------------------------------------
Ran 1 test in 0.016s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.
----------------------------------------------------------------------
Ran 1 test in 0.015s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.
----------------------------------------------------------------------
Ran 1 test in 0.014s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.
----------------------------------------------------------------------
Ran 1 test in 0.015s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.
----------------------------------------------------------------------
Ran 1 test in 0.029s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
E
======================================================================
ERROR: test_collatz (__main__.TestMinimum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_minimum.py", line 11, in test_collatz
    the_minimum.collatz('hello')
  File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 18, in collatz
    if x % 2 == 0:
TypeError: not all arguments converted during string formatting

----------------------------------------------------------------------
Ran 1 test in 0.023s

FAILED (errors=1)
>>> 
>>> 3 + 4
7
>>> 3 + 'hello'
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    3 + 'hello'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
..
----------------------------------------------------------------------
Ran 2 tests in 0.034s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.E
======================================================================
ERROR: test_employee (__main__.TestMinimum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_minimum.py", line 18, in test_employee
    navra = the_minimum.Employee('Navra Ananda', 200)
TypeError: __init__() missing 1 required positional argument: 'salary'

----------------------------------------------------------------------
Ran 2 tests in 0.031s

FAILED (errors=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.E
======================================================================
ERROR: test_employee (__main__.TestMinimum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_minimum.py", line 20, in test_employee
    self.assertEqual(navra.female, 'female')
AttributeError: 'Employee' object has no attribute 'female'

----------------------------------------------------------------------
Ran 2 tests in 0.033s

FAILED (errors=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
..
----------------------------------------------------------------------
Ran 2 tests in 0.034s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.F
======================================================================
FAIL: test_employee (__main__.TestMinimum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_minimum.py", line 23, in test_employee
    self.assertEqual(navra.salary, 220)
AssertionError: 220.00000000000003 != 220

----------------------------------------------------------------------
Ran 2 tests in 0.037s

FAILED (failures=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.F
======================================================================
FAIL: test_employee (__main__.TestMinimum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_minimum.py", line 23, in test_employee
    self.assertEqual(navra.salary, 220)
AssertionError: 200 != 220

----------------------------------------------------------------------
Ran 2 tests in 0.041s

FAILED (failures=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
.E
======================================================================
ERROR: test_employee (__main__.TestMinimum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_minimum.py", line 22, in test_employee
    navra.give_raise(10)
  File "/Users/raymond/Dropbox/Public/sj164/the_minimum.py", line 42, in give_raise
    self = salary * (100 + percentage) // 100
NameError: name 'salary' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.044s

FAILED (errors=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46
male
male
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
..
----------------------------------------------------------------------
Ran 2 tests in 0.027s

OK
>>> 
>>> salary = 200
>>> 1 + 20
21
>>> (1 + 20) // 100
0
>>> (1 + 20) / 100
0.21
>>> (100 + 20)
120
>>> (100 + 20) / 100
1.2
>>> (100 + 20) // 100
1
>>> salary * (100 + 20) // 100
240
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
..
----------------------------------------------------------------------
Ran 2 tests in 0.032s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.050s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.048s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.048s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.048s

OK
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/test_minimum.py ========
...
----------------------------------------------------------------------
Ran 3 tests in 0.056s

OK
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 19, in <module>
    test = FrameworkTest('some_method')
NameError: name 'FrameworkTest' is not defined
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 22, in <module>
    test = FrameworkTest('some_method')
TypeError: object() takes no parameters
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 25, in <module>
    print(test.was_run, '<-- this should be False')
AttributeError: 'FrameworkTest' object has no attribute 'was_run'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 27, in <module>
    test.some_method()
AttributeError: 'FrameworkTest' object has no attribute 'some_method'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
False <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
>>> test = FrameworkTest('some_method')
>>> type(test)
<class '__main__.FrameworkTest'>
>>> vars(test)
{'method_name': 'some_method', 'was_run': False}
>>> test.some_method()
>>> vars(test)
{'method_name': 'some_method', 'was_run': True}
>>> test.was_run
True
>>> # RED - > GREEN -> Refactor/Generalize
>>> 
>>> # square(x) -> 9           square(x)   x**2
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 35, in <module>
    test.some_othermethod()
AttributeError: 'FrameworkTest' object has no attribute 'some_othermethod'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 35, in <module>
    test.some_other_method()
AttributeError: 'FrameworkTest' object has no attribute 'some_other_method'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 39, in <module>
    test.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 28, in run
    method = getattr(self, self.method_name)
AttributeError: 'FrameworkTest' object has no attribute 'some_other_method'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
>>> 
>>> 
>>> assert 5 + 3 == 8
>>> assert 5 + 3 == 10
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    assert 5 + 3 == 10
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
False <-- this should be False
True <-- this should be True
False <-- this should be False
True <-- this should be True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 46, in <module>
    assert test.was_run == True
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> dir()
['FrameworkTest', 'TestCase', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'test']
>>> test.was_run
True
>>> getattr(test, 'was_run')
True
>>> getattr(test, 'was_not_run')
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    getattr(test, 'was_not_run')
AttributeError: 'FrameworkTest' object has no attribute 'was_not_run'
>>> getattr(test, 'was_not_run', False)
False
>>> None
>>> print(getattr(test, 'was_not_run', None))
None
>>> False
False
>>> None
>>> 30 + 40
70
>>> None
>>> getattr(test, 'was_not_run', None)
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 44, in <module>
    assert test.was_setup == False
AttributeError: 'FrameworkTest' object has no attribute 'was_setup'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 47, in <module>
    assert test.was_setup == True
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 50, in <module>
    assert test.was_setup == True
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 53, in <module>
    assert test.was_setup == True
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 65, in <module>
    test.test_running()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 34, in test_running
    self.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 28, in run
    method()
TypeError: 'NoneType' object is not callable
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 60, in <module>
    assert test.was_torn_down == False
AttributeError: 'FrameworkTest' object has no attribute 'was_torn_down'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 64, in <module>
    assert test.was_torn_down == True
AssertionError
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj164/beck.py ============
Done!
>>> 
>>> 
>>> 
