Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # Fluent Python  <-- Philosophically Aligned
>>> # Coding Club    <-- Obstensibly are for funs.  Best written Python books ever.
>>> # Programming Pearls and More Programming Pearls <-- Jon Bentley.
>>> # The Python Essential Reference <-- David Beazley
>>> # How to Solve It <-- Polya    (available for free)
>>> 
>>> ###################################################
>>> # Finish the dict exercise
>>> # Parse column oriented text
>>> # List comprehensions
>>> # Regular expressions
>>> # REST API
>>> # Special Requests -- Open Mike
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['bill'] = 'matrix'
>>> d['bob'] = 'usual suspects'
>>> d['cindy'] = 'driving miss daisy'
>>> 
>>> d.n
8
>>> d.desks
[[], [], [], ['bill', 'bob'], [], [], [], ['cindy']]
>>> d.folders
[[], [], [], ['matrix', 'usual suspects'], [], [], [], ['driving miss daisy']]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 32, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 24, in test_lookup
    assert d['philip'] == 'white'
TypeError: 'Dict' object is not subscriptable
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 32, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 24, in test_lookup
    assert d['philip'] == 'white'
TypeError: 'Dict' object is not subscriptable
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_lookup
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 24, in test_lookup
    assert d['philip'] == 'white'
AssertionError
..
3 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_lookup
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 28, in test_lookup
    d['craig']
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 27, in __getitem__
    j = desk.index(key)
ValueError: 'craig' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 28, in test_lookup
    d['craig']
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 40, in __exit__
    assert False, f'Expected {self.exception}'
AssertionError: Expected <class 'KeyError'>
..
3 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
...
3 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 49, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 32, in test_membership
    assert 'philip' not in d
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 24, in __getitem__
    i = myhash(key) % self.n
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 6, in myhash
    for c in s:
TypeError: 'int' object is not iterable
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..ERROR:root:Test failed: test_membership
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 41, in test_membership
    assert 'philip' in d
AssertionError
..
4 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
....
4 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 72, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 58, in test_deletion
    del d['philip']
AttributeError: __delitem__
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_deletion
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 59, in test_deletion
    assert 'philip' not in d
AssertionError
....
5 run, 1 failed
>>> # d[k]       ==>  d.__getitem__(k)
>>> # d[k] = v   ==>  d.__setitem__(k, v)
>>> # del d[k]   ==>  d.__delitem__(k)
>>> 
>>> 
>>> d = dict(raymond='red', rachel='blue')
>>> d['raymond']
'red'
>>> d.__getitem__('raymond')
'red'
>>> 
>>> d['raymond'] = 'orange'
>>> d
{'raymond': 'orange', 'rachel': 'blue'}
>>> d.__setitem__('raymond', 'orange')
>>> 
>>> del d['raymond']
>>> d
{'rachel': 'blue'}
>>> 
>>> desk = ['bob', 'tom', 'kevin', 'mark']
>>> folder = ['red', 'green', 'blue', 'orange']
>>> 
>>> key = 'kevin'
>>> j = desk.index(key)
>>> j
2
>>> del desk[j]
>>> desk
['bob', 'tom', 'mark']
>>> del folder[j]
>>> folder
['red', 'green', 'orange']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.....
5 run, 0 failed
>>> desk = ['bob', 'tom', 'kevin', 'mark']
>>> type(desk)
<class 'list'>
>>> help(desk.index)
Help on built-in function index:

index(...) method of builtins.list instance
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['raymond']
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 28, in __getitem__
    j = desk.index(key)
ValueError: 'raymond' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d['raymond']
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 30, in __getitem__
    raise KeyError(key)
KeyError: 'raymond'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['raymond']
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 28, in __getitem__
    j = desk.index(key)
ValueError: 'raymond' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d['raymond']
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 30, in __getitem__
    raise KeyError(key)
KeyError: 'raymond'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['raymond']
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 28, in __getitem__
    j = desk.index(key)
ValueError: 'raymond' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    d['raymond']
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 30, in __getitem__
    raise KeyError(key)
KeyError: 'raymond'
>>> del d['raymond']
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 45, in __delitem__
    j = desk.index(key)
ValueError: 'raymond' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    del d['raymond']
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 47, in __delitem__
    raise KeyError
KeyError
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.....
5 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 92, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 72, in test_len
    assert len(d) == 0
TypeError: object of type 'Dict' has no len()
>>> desks = [[], [], [], ['bill', 'bob'], [], [], [], ['cindy']]
>>> 0 + 0 + 0 + 2 + 0 + 0 + 0 + 1
3
>>> for desk in desks:
	print(desk)

	
[]
[]
[]
['bill', 'bob']
[]
[]
[]
['cindy']
>>> for desk in desks:
	print(len(desk))

	
0
0
0
2
0
0
0
1
>>> [len(desk) for desk in desks]
[0, 0, 0, 2, 0, 0, 0, 1]
>>> sum([len(desk) for desk in desks])
3
>>> sum([10, 20, 30])
60
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..ERROR:root:Test failed: test_len
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 74, in test_len
    assert len(d) == 1
AssertionError
....
6 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> # DRY -- Do not repeat yourself
>>> #  \-> Need to refactor
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 2, in <module>
    from dictionary import Dict, myhash
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 16
    def _get_desk_and_folder(self, key)
                                      ^
SyntaxError: invalid syntax
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 2, in <module>
    from dictionary import Dict, myhash
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 22
    def _find_position_at_a_desk(self, key, desk)
                                                ^
SyntaxError: invalid syntax
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......
6 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['raymond'] = 'red'
>>> d['rachel'] = 'blue'
>>> d['rachel'] = 'azure'
>>> d['raymond']
'red'
>>> d['rachel']
'blue'
>>> d.desks
[[], [], ['raymond'], [], [], [], [], ['rachel', 'rachel']]
>>> d.folders
[[], [], ['red'], [], [], [], [], ['blue', 'azure']]
>>> len(d)
3
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
......ERROR:root:Test failed: test_set_twice_bug
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 96, in test_set_twice_bug
    assert d['rachel'] == 'azure'
AssertionError
.
7 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.......
7 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_deletion
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 53, in test_deletion
    assert 'philip' in d
AssertionError
.ERROR:root:Test failed: test_len
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 74, in test_len
    assert len(d) == 1
AssertionError
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 24, in _find_position_at_a_desk
    return desk.index(key)
ValueError: 'philip' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 102, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 24, in test_lookup
    assert d['philip'] == 'white'
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 41, in __getitem__
    j = self._find_position_at_a_desk(key, desk)
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 26, in _find_position_at_a_desk
    raise KeyError(key)
KeyError: 'philip'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.......
7 run, 0 failed
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj164/the_minimum.py ========
TestResults(failed=0, attempted=2)
46
male
male
>>> import requests
>>> r = requests.get('https://api.github.com/users/raymondh')
>>> r.status_code
200
>>> r.headers
{'Date': 'Thu, 13 Jul 2017 18:58:01 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Server': 'GitHub.com', 'Status': '200 OK', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '53', 'X-RateLimit-Reset': '1499974821', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding', 'ETag': 'W/"a8b2d7c89c6d4d93b973a2b3973ef837"', 'Last-Modified': 'Thu, 19 Feb 2015 23:15:19 GMT', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Access-Control-Expose-Headers': 'ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval', 'Access-Control-Allow-Origin': '*', 'Content-Security-Policy': "default-src 'none'", 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'deny', 'X-XSS-Protection': '1; mode=block', 'X-Runtime-rack': '0.041390', 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': 'CB07:227F7:E643:11484:5967C2B9'}
>>> r.content
b'{"login":"raymondh","id":167559,"avatar_url":"https://avatars0.githubusercontent.com/u/167559?v=3","gravatar_id":"","url":"https://api.github.com/users/raymondh","html_url":"https://github.com/raymondh","followers_url":"https://api.github.com/users/raymondh/followers","following_url":"https://api.github.com/users/raymondh/following{/other_user}","gists_url":"https://api.github.com/users/raymondh/gists{/gist_id}","starred_url":"https://api.github.com/users/raymondh/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/raymondh/subscriptions","organizations_url":"https://api.github.com/users/raymondh/orgs","repos_url":"https://api.github.com/users/raymondh/repos","events_url":"https://api.github.com/users/raymondh/events{/privacy}","received_events_url":"https://api.github.com/users/raymondh/received_events","type":"User","site_admin":false,"name":"Raymond Hettinger","company":"SauceLabs","blog":"","location":"Los Angeles and San Francisco California","email":null,"hireable":null,"bio":null,"public_repos":0,"public_gists":0,"followers":114,"following":0,"created_at":"2009-12-14T20:09:05Z","updated_at":"2015-02-19T23:15:19Z"}'
>>> info = r.json()
>>> type(info)
<class 'dict'>
>>> info.keys()
dict_keys(['login', 'id', 'avatar_url', 'gravatar_id', 'url', 'html_url', 'followers_url', 'following_url', 'gists_url', 'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url', 'events_url', 'received_events_url', 'type', 'site_admin', 'name', 'company', 'blog', 'location', 'email', 'hireable', 'bio', 'public_repos', 'public_gists', 'followers', 'following', 'created_at', 'updated_at'])
>>> info['company']
'SauceLabs'
>>> info['name']
'Raymond Hettinger'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj164/github_rest_api.py ======
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/github_rest_api.py", line 8, in <module>
    info = r.json()
  File "/Users/raymond/Dropbox/Public/sj164/tddpython/lib/python3.6/site-packages/requests/models.py", line 894, in json
    return complexjson.loads(self.text, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/__init__.py", line 354, in loads
    return _default_decoder.decode(s)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/decoder.py", line 339, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/json/decoder.py", line 357, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj164/github_rest_api.py ======
Raymond Hettinger works at SauceLabs. Contact at None
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj164/github_rest_api.py ======
Raymond Hettinger works at SauceLabs. Contact at None
>>> 
>>> 
>>> 
>>> 'The answer is {0} today'.format(10)
'The answer is 10 today'
>>> 'The answer is {0} today but was {1} yesterday'.format(10, 20)
'The answer is 10 today but was 20 yesterday'
>>> #                                                       0   1
>>> 'The answer is {1} today but was {0} yesterday'.format(10, 20)
'The answer is 20 today but was 10 yesterday'
>>> 'The answer is {1} today but was {1} yesterday'.format(10, 20)
'The answer is 20 today but was 20 yesterday'
>>> 'The answer is {new} today but was {old} yesterday'.format(new=10, old=20)
'The answer is 10 today but was 20 yesterday'
>>> 
>>> info = {'new': 10, 'old': 20}
>>> 'The answer is {new} today but was {old} yesterday'.format(new=info['new'], old=info['old'])
'The answer is 10 today but was 20 yesterday'
>>> 'The answer is {new} today but was {old} yesterday'.format(**info)
'The answer is 10 today but was 20 yesterday'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj164/github_rest_api.py ======
Raymond Hettinger works at SauceLabs. Contact at None
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj164/github_rest_api.py ======
Raymond Hettinger works at SauceLabs. Contact at None
Jason Huggins works at None. Contact at None
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> myhash('raymond')
2900084602
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> myhash('raymond')
62165368770632863968
>>> myhash('raymond')
62165368770632863968
>>> myhash('raymond')
62165368770632863968
>>> 
=============================== RESTART: Shell ===============================
>>> myhash('raymond')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    myhash('raymond')
NameError: name 'myhash' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> myhash('raymond')
62165369947073839459
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
........
8 run, 0 failed
>>> myhash('raymond')
62165380346286829298
>>> myhash('raymond')
62165380346286829298
>>> 
=============================== RESTART: Shell ===============================
>>> myhash('raymond')
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    myhash('raymond')
NameError: name 'myhash' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> myhash('raymond')
62165387237104164987
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
........
8 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 122, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 116, in test_clear
    d.clear()
AttributeError: 'Dict' object has no attribute 'clear'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.ERROR:root:Test failed: test_clear
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 117, in test_clear
    assert len(d) == 0
AssertionError
........
9 run, 1 failed
>>> 
>>> 
>>> s = ['raymond', 'rachel', 'matthew']
>>> s.clear()
>>> s
[]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 122, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 116, in test_clear
    d.clear()
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 66, in clear
    for desk in self.desks():
TypeError: 'list' object is not callable
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 122, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 116, in test_clear
    d.clear()
  File "/Users/raymond/Dropbox/Public/sj164/dictionary.py", line 66, in clear
    for desk in self.desks():
TypeError: 'list' object is not callable
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
.........
9 run, 0 failed
>>> s = ['raymond', 'rachel', 'matthew']
>>> s()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    s()
TypeError: 'list' object is not callable
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dict(raymond='red', rachel='blue')
{'raymond': 'red', 'rachel': 'blue'}
>>> d = dict(raymond='red', rachel='blue')
>>> for k in d.keys():
	print(k)

	
raymond
rachel
>>> for k in d.keys():
	print(k, d[k])

	
raymond red
rachel blue
>>> for k in d.keys():
	print(f'{k}: {d[k]}')

	
raymond: red
rachel: blue
>>> s = 'raymond'
>>> print(str(s))
raymond
>>> print(repr(s))
'raymond'
>>> for k in d.keys():
	print(f'{k!r}: {d[k]!r}')

	
'raymond': 'red'
'rachel': 'blue'
>>> [f'{k!r}: {d[k]!r}' for k in d.keys()]
["'raymond': 'red'", "'rachel': 'blue'"]
>>> ', '.join([f'{k!r}: {d[k]!r}' for k in d.keys()])
"'raymond': 'red', 'rachel': 'blue'"
>>> print( ', '.join([f'{k!r}: {d[k]!r}' for k in d.keys()]) )
'raymond': 'red', 'rachel': 'blue'
>>> print( '{' + ', '.join([f'{k!r}: {d[k]!r}' for k in d.keys()])  + '}' )
{'raymond': 'red', 'rachel': 'blue'}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
...Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 134, in <module>
    beck.run_tests(TestDict)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 107, in run_tests
    suite.run(result)
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 86, in run
    testcase.run()
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 125, in test_keys
    assert sorted(d.keys()) == sorted([('philip', 'white'),
AttributeError: 'Dict' object has no attribute 'keys'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
...ERROR:root:Test failed: test_keys
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 128, in test_keys
    ('rucha', 'green')])
AssertionError
.......
10 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['philip'] = 'white'
>>> d.keys()
['philip']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
...ERROR:root:Test failed: test_keys
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/beck.py", line 59, in run
    test_method()
  File "/Users/raymond/Dropbox/Public/sj164/test_dict.py", line 125, in test_keys
    assert sorted(d.keys()) == sorted(['philip', 'rama', 'alejandro', 'blue'])
AssertionError
.......
10 run, 1 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..........
10 run, 0 failed
>>> d = Dict()
>>> d.keys()
[]
>>> d['philip'] = 'white'
>>> d.keys()
['philip']
>>> d['rama'] = 'white'
>>> d.keys()
['philip', 'rama']
>>> d['alejandro'] = 'blue'
>>> d.keys()
['philip', 'alejandro', 'rama']
>>> d.desks
[[], [], [], ['philip'], [], ['alejandro'], ['rama'], []]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d
{}
>>> d['philip'] = 'white'
>>> d
{'philip'}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d
{}
>>> d['philip'] = 'white'
>>> d
{'philip': 'white'}
>>> d['rama'] = 'white'
>>> d
{'rama': 'white', 'philip': 'white'}
>>> d['alejandro'] = 'blue'
>>> d
{'alejandro': 'blue', 'rama': 'white', 'philip': 'white'}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/dictionary.py =========
>>> d = Dict()
>>> d['philip'] = 'white'
>>> d['rama'] = 'white'
>>> d['alejandro'] = 'blue'
>>> d
{'philip': 'white', 'alejandro': 'blue', 'rama': 'white'}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/test_dict.py =========
..........
10 run, 0 failed
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
Interface                      IP-Address      Status                Protocol
Loopback0                      51.51.51.51     Up                    Up
MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up
MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down
MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up
HundredGigE0/1/0/0             unassigned      Shutdown              Down
HundredGigE0/1/0/1             unassigned      Shutdown              Down
TenGigE0/2/0/0                 unassigned      Down                  Down
TenGigE0/2/0/1                 unassigned      Down                  Down
TenGigE0/2/0/2                 unassigned      Down                  Down
TenGigE0/2/0/4                 unassigned      Down                  Down
TenGigE0/2/0/5                 unassigned      Down                  Down
TenGigE0/2/0/6                 unassigned      Down                  Down
TenGigE0/2/0/7                 unassigned      Down                  Down
GigabitEthernet0/3/0/1         unassigned      Up                    Up
GigabitEthernet0/3/0/2         unassigned      Down                  Down
GigabitEthernet0/3/0/3         unassigned      Up                    Up
GigabitEthernet0/3/0/4         unassigned      Down                  Down
GigabitEthernet0/3/0/5         unassigned      Down                  Down
GigabitEthernet0/3/0/6         unassigned      Down                  Down
GigabitEthernet0/3/0/7         unassigned      Down                  Down
GigabitEthernet0/3/0/8         unassigned      Down                  Down
GigabitEthernet0/3/0/9         unassigned      Down                  Down
GigabitEthernet0/3/0/10        unassigned      Down                  Down
GigabitEthernet0/3/0/11        unassigned      Down                  Down
GigabitEthernet0/3/0/12        unassigned      Down                  Down
GigabitEthernet0/3/0/13        unassigned      Down                  Down
GigabitEthernet0/3/0/14        unassigned      Down                  Down
GigabitEthernet0/3/0/15        unassigned      Down                  Down
GigabitEthernet0/3/0/16        unassigned      Down                  Down
GigabitEthernet0/3/0/17        unassigned      Down                  Down
GigabitEthernet0/3/0/18        unassigned      Down                  Down
GigabitEthernet0/3/0/19        unassigned      Down                  Down
TenGigE0/3/1/0                 unassigned      Up                    Up
TenGigE0/3/1/1                 unassigned      Down                  Down
TenGigE0/3/1/2                 unassigned      Down                  Down
TenGigE0/3/1/3                 unassigned      Up                    Up
GigabitEthernet0/4/0/0         unassigned      Down                  Down
TenGigE0/4/0/0                 unassigned      Up                    Up
GigabitEthernet0/4/0/1         unassigned      Down                  Down
TenGigE0/4/0/1                 unassigned      Down                  Down
GigabitEthernet0/4/0/2         unassigned      Down                  Down
GigabitEthernet0/4/0/3         unassigned      Down                  Down
GigabitEthernet0/4/0/4         unassigned      Down                  Down
GigabitEthernet0/4/0/5         unassigned      Down                  Down
GigabitEthernet0/4/0/6         unassigned      Down                  Down
GigabitEthernet0/4/0/7         unassigned      Down                  Down
GigabitEthernet0/4/0/8         unassigned      Down                  Down
GigabitEthernet0/4/0/9         unassigned      Down                  Down
GigabitEthernet0/4/0/10        unassigned      Down                  Down
GigabitEthernet0/4/0/11        unassigned      Down                  Down
GigabitEthernet0/4/0/12        unassigned      Down                  Down
GigabitEthernet0/4/0/13        unassigned      Down                  Down
GigabitEthernet0/4/0/14        unassigned      Down                  Down
GigabitEthernet0/4/0/15        unassigned      Down                  Down
GigabitEthernet0/4/0/16        unassigned      Down                  Down
GigabitEthernet0/4/0/17        unassigned      Down                  Down
GigabitEthernet0/4/0/18        unassigned      Down                  Down
GigabitEthernet0/4/0/19        unassigned      Down                  Down
FortyGigE0/5/0/0               unassigned      Shutdown              Down
FortyGigE0/5/0/1               unassigned      Shutdown              Down
TenGigE0/5/1/0                 unassigned      Shutdown              Down
TenGigE0/5/1/1                 111.1.1.1       Up                    Up
GigabitEthernet0/7/0/0         unassigned      Down                  Down
GigabitEthernet0/7/0/1         unassigned      Down                  Down
GigabitEthernet0/7/0/2         unassigned      Down                  Down
GigabitEthernet0/7/0/3         unassigned      Down                  Down
GigabitEthernet0/7/0/4         unassigned      Down                  Down
GigabitEthernet0/7/0/5         unassigned      Down                  Down
GigabitEthernet0/7/0/6         unassigned      Down                  Down
GigabitEthernet0/7/0/7         unassigned      Down                  Down
GigabitEthernet0/7/0/8         unassigned      Down                  Down
GigabitEthernet0/7/0/9         unassigned      Down                  Down
GigabitEthernet0/7/0/10        unassigned      Down                  Down
GigabitEthernet0/7/0/11        unassigned      Down                  Down
GigabitEthernet0/7/0/12        unassigned      Down                  Down
GigabitEthernet0/7/0/13        unassigned      Down                  Down
GigabitEthernet0/7/0/14        unassigned      Down                  Down
GigabitEthernet0/7/0/15        unassigned      Up                    Up
GigabitEthernet0/7/0/16        unassigned      Down                  Down
GigabitEthernet0/7/0/17        unassigned      Down                  Down
GigabitEthernet0/7/0/18        unassigned      Down                  Down
GigabitEthernet0/7/0/19        unassigned      Down                  Down
GigabitEthernet0/7/0/20        unassigned      Down                  Down
GigabitEthernet0/7/0/21        unassigned      Down                  Down
GigabitEthernet0/7/0/22        unassigned      Down                  Down
GigabitEthernet0/7/0/23        unassigned      Down                  Down
GigabitEthernet0/7/0/24        unassigned      Down                  Down
GigabitEthernet0/7/0/25        unassigned      Down                  Down
GigabitEthernet0/7/0/26        unassigned      Down                  Down
GigabitEthernet0/7/0/27        unassigned      Down                  Down
GigabitEthernet0/7/0/28        unassigned      Down                  Down
GigabitEthernet0/7/0/29        unassigned      Down                  Down
GigabitEthernet0/7/0/30        unassigned      Down                  Down
GigabitEthernet0/7/0/31        unassigned      Down                  Down
GigabitEthernet0/7/0/32        unassigned      Down                  Down
GigabitEthernet0/7/0/33        unassigned      Down                  Down
GigabitEthernet0/7/0/34        unassigned      Down                  Down
GigabitEthernet0/7/0/35        unassigned      Down                  Down
GigabitEthernet0/7/0/36        unassigned      Down                  Down
GigabitEthernet0/7/0/37        unassigned      Down                  Down
GigabitEthernet0/7/0/38        unassigned      Down                  Down
GigabitEthernet0/7/0/39        unassigned      Down                  Down

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
Interface                      IP-Address      Status                Protocol

Loopback0                      51.51.51.51     Up                    Up

MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up

MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down

MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up

HundredGigE0/1/0/0             unassigned      Shutdown              Down

HundredGigE0/1/0/1             unassigned      Shutdown              Down

TenGigE0/2/0/0                 unassigned      Down                  Down

TenGigE0/2/0/1                 unassigned      Down                  Down

TenGigE0/2/0/2                 unassigned      Down                  Down

TenGigE0/2/0/4                 unassigned      Down                  Down

TenGigE0/2/0/5                 unassigned      Down                  Down

TenGigE0/2/0/6                 unassigned      Down                  Down

TenGigE0/2/0/7                 unassigned      Down                  Down

GigabitEthernet0/3/0/1         unassigned      Up                    Up

GigabitEthernet0/3/0/2         unassigned      Down                  Down

GigabitEthernet0/3/0/3         unassigned      Up                    Up

GigabitEthernet0/3/0/4         unassigned      Down                  Down

GigabitEthernet0/3/0/5         unassigned      Down                  Down

GigabitEthernet0/3/0/6         unassigned      Down                  Down

GigabitEthernet0/3/0/7         unassigned      Down                  Down

GigabitEthernet0/3/0/8         unassigned      Down                  Down

GigabitEthernet0/3/0/9         unassigned      Down                  Down

GigabitEthernet0/3/0/10        unassigned      Down                  Down

GigabitEthernet0/3/0/11        unassigned      Down                  Down

GigabitEthernet0/3/0/12        unassigned      Down                  Down

GigabitEthernet0/3/0/13        unassigned      Down                  Down

GigabitEthernet0/3/0/14        unassigned      Down                  Down

GigabitEthernet0/3/0/15        unassigned      Down                  Down

GigabitEthernet0/3/0/16        unassigned      Down                  Down

GigabitEthernet0/3/0/17        unassigned      Down                  Down

GigabitEthernet0/3/0/18        unassigned      Down                  Down

GigabitEthernet0/3/0/19        unassigned      Down                  Down

TenGigE0/3/1/0                 unassigned      Up                    Up

TenGigE0/3/1/1                 unassigned      Down                  Down

TenGigE0/3/1/2                 unassigned      Down                  Down

TenGigE0/3/1/3                 unassigned      Up                    Up

GigabitEthernet0/4/0/0         unassigned      Down                  Down

TenGigE0/4/0/0                 unassigned      Up                    Up

GigabitEthernet0/4/0/1         unassigned      Down                  Down

TenGigE0/4/0/1                 unassigned      Down                  Down

GigabitEthernet0/4/0/2         unassigned      Down                  Down

GigabitEthernet0/4/0/3         unassigned      Down                  Down

GigabitEthernet0/4/0/4         unassigned      Down                  Down

GigabitEthernet0/4/0/5         unassigned      Down                  Down

GigabitEthernet0/4/0/6         unassigned      Down                  Down

GigabitEthernet0/4/0/7         unassigned      Down                  Down

GigabitEthernet0/4/0/8         unassigned      Down                  Down

GigabitEthernet0/4/0/9         unassigned      Down                  Down

GigabitEthernet0/4/0/10        unassigned      Down                  Down

GigabitEthernet0/4/0/11        unassigned      Down                  Down

GigabitEthernet0/4/0/12        unassigned      Down                  Down

GigabitEthernet0/4/0/13        unassigned      Down                  Down

GigabitEthernet0/4/0/14        unassigned      Down                  Down

GigabitEthernet0/4/0/15        unassigned      Down                  Down

GigabitEthernet0/4/0/16        unassigned      Down                  Down

GigabitEthernet0/4/0/17        unassigned      Down                  Down

GigabitEthernet0/4/0/18        unassigned      Down                  Down

GigabitEthernet0/4/0/19        unassigned      Down                  Down

FortyGigE0/5/0/0               unassigned      Shutdown              Down

FortyGigE0/5/0/1               unassigned      Shutdown              Down

TenGigE0/5/1/0                 unassigned      Shutdown              Down

TenGigE0/5/1/1                 111.1.1.1       Up                    Up

GigabitEthernet0/7/0/0         unassigned      Down                  Down

GigabitEthernet0/7/0/1         unassigned      Down                  Down

GigabitEthernet0/7/0/2         unassigned      Down                  Down

GigabitEthernet0/7/0/3         unassigned      Down                  Down

GigabitEthernet0/7/0/4         unassigned      Down                  Down

GigabitEthernet0/7/0/5         unassigned      Down                  Down

GigabitEthernet0/7/0/6         unassigned      Down                  Down

GigabitEthernet0/7/0/7         unassigned      Down                  Down

GigabitEthernet0/7/0/8         unassigned      Down                  Down

GigabitEthernet0/7/0/9         unassigned      Down                  Down

GigabitEthernet0/7/0/10        unassigned      Down                  Down

GigabitEthernet0/7/0/11        unassigned      Down                  Down

GigabitEthernet0/7/0/12        unassigned      Down                  Down

GigabitEthernet0/7/0/13        unassigned      Down                  Down

GigabitEthernet0/7/0/14        unassigned      Down                  Down

GigabitEthernet0/7/0/15        unassigned      Up                    Up

GigabitEthernet0/7/0/16        unassigned      Down                  Down

GigabitEthernet0/7/0/17        unassigned      Down                  Down

GigabitEthernet0/7/0/18        unassigned      Down                  Down

GigabitEthernet0/7/0/19        unassigned      Down                  Down

GigabitEthernet0/7/0/20        unassigned      Down                  Down

GigabitEthernet0/7/0/21        unassigned      Down                  Down

GigabitEthernet0/7/0/22        unassigned      Down                  Down

GigabitEthernet0/7/0/23        unassigned      Down                  Down

GigabitEthernet0/7/0/24        unassigned      Down                  Down

GigabitEthernet0/7/0/25        unassigned      Down                  Down

GigabitEthernet0/7/0/26        unassigned      Down                  Down

GigabitEthernet0/7/0/27        unassigned      Down                  Down

GigabitEthernet0/7/0/28        unassigned      Down                  Down

GigabitEthernet0/7/0/29        unassigned      Down                  Down

GigabitEthernet0/7/0/30        unassigned      Down                  Down

GigabitEthernet0/7/0/31        unassigned      Down                  Down

GigabitEthernet0/7/0/32        unassigned      Down                  Down

GigabitEthernet0/7/0/33        unassigned      Down                  Down

GigabitEthernet0/7/0/34        unassigned      Down                  Down

GigabitEthernet0/7/0/35        unassigned      Down                  Down

GigabitEthernet0/7/0/36        unassigned      Down                  Down

GigabitEthernet0/7/0/37        unassigned      Down                  Down

GigabitEthernet0/7/0/38        unassigned      Down                  Down

GigabitEthernet0/7/0/39        unassigned      Down                  Down

>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down\n'
>>> print(line)
GigabitEthernet0/7/0/39        unassigned      Down                  Down

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
Interface                      IP-Address      Status                Protocol
Loopback0                      51.51.51.51     Up                    Up
MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up
MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down
MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up
HundredGigE0/1/0/0             unassigned      Shutdown              Down
HundredGigE0/1/0/1             unassigned      Shutdown              Down
TenGigE0/2/0/0                 unassigned      Down                  Down
TenGigE0/2/0/1                 unassigned      Down                  Down
TenGigE0/2/0/2                 unassigned      Down                  Down
TenGigE0/2/0/4                 unassigned      Down                  Down
TenGigE0/2/0/5                 unassigned      Down                  Down
TenGigE0/2/0/6                 unassigned      Down                  Down
TenGigE0/2/0/7                 unassigned      Down                  Down
GigabitEthernet0/3/0/1         unassigned      Up                    Up
GigabitEthernet0/3/0/2         unassigned      Down                  Down
GigabitEthernet0/3/0/3         unassigned      Up                    Up
GigabitEthernet0/3/0/4         unassigned      Down                  Down
GigabitEthernet0/3/0/5         unassigned      Down                  Down
GigabitEthernet0/3/0/6         unassigned      Down                  Down
GigabitEthernet0/3/0/7         unassigned      Down                  Down
GigabitEthernet0/3/0/8         unassigned      Down                  Down
GigabitEthernet0/3/0/9         unassigned      Down                  Down
GigabitEthernet0/3/0/10        unassigned      Down                  Down
GigabitEthernet0/3/0/11        unassigned      Down                  Down
GigabitEthernet0/3/0/12        unassigned      Down                  Down
GigabitEthernet0/3/0/13        unassigned      Down                  Down
GigabitEthernet0/3/0/14        unassigned      Down                  Down
GigabitEthernet0/3/0/15        unassigned      Down                  Down
GigabitEthernet0/3/0/16        unassigned      Down                  Down
GigabitEthernet0/3/0/17        unassigned      Down                  Down
GigabitEthernet0/3/0/18        unassigned      Down                  Down
GigabitEthernet0/3/0/19        unassigned      Down                  Down
TenGigE0/3/1/0                 unassigned      Up                    Up
TenGigE0/3/1/1                 unassigned      Down                  Down
TenGigE0/3/1/2                 unassigned      Down                  Down
TenGigE0/3/1/3                 unassigned      Up                    Up
GigabitEthernet0/4/0/0         unassigned      Down                  Down
TenGigE0/4/0/0                 unassigned      Up                    Up
GigabitEthernet0/4/0/1         unassigned      Down                  Down
TenGigE0/4/0/1                 unassigned      Down                  Down
GigabitEthernet0/4/0/2         unassigned      Down                  Down
GigabitEthernet0/4/0/3         unassigned      Down                  Down
GigabitEthernet0/4/0/4         unassigned      Down                  Down
GigabitEthernet0/4/0/5         unassigned      Down                  Down
GigabitEthernet0/4/0/6         unassigned      Down                  Down
GigabitEthernet0/4/0/7         unassigned      Down                  Down
GigabitEthernet0/4/0/8         unassigned      Down                  Down
GigabitEthernet0/4/0/9         unassigned      Down                  Down
GigabitEthernet0/4/0/10        unassigned      Down                  Down
GigabitEthernet0/4/0/11        unassigned      Down                  Down
GigabitEthernet0/4/0/12        unassigned      Down                  Down
GigabitEthernet0/4/0/13        unassigned      Down                  Down
GigabitEthernet0/4/0/14        unassigned      Down                  Down
GigabitEthernet0/4/0/15        unassigned      Down                  Down
GigabitEthernet0/4/0/16        unassigned      Down                  Down
GigabitEthernet0/4/0/17        unassigned      Down                  Down
GigabitEthernet0/4/0/18        unassigned      Down                  Down
GigabitEthernet0/4/0/19        unassigned      Down                  Down
FortyGigE0/5/0/0               unassigned      Shutdown              Down
FortyGigE0/5/0/1               unassigned      Shutdown              Down
TenGigE0/5/1/0                 unassigned      Shutdown              Down
TenGigE0/5/1/1                 111.1.1.1       Up                    Up
GigabitEthernet0/7/0/0         unassigned      Down                  Down
GigabitEthernet0/7/0/1         unassigned      Down                  Down
GigabitEthernet0/7/0/2         unassigned      Down                  Down
GigabitEthernet0/7/0/3         unassigned      Down                  Down
GigabitEthernet0/7/0/4         unassigned      Down                  Down
GigabitEthernet0/7/0/5         unassigned      Down                  Down
GigabitEthernet0/7/0/6         unassigned      Down                  Down
GigabitEthernet0/7/0/7         unassigned      Down                  Down
GigabitEthernet0/7/0/8         unassigned      Down                  Down
GigabitEthernet0/7/0/9         unassigned      Down                  Down
GigabitEthernet0/7/0/10        unassigned      Down                  Down
GigabitEthernet0/7/0/11        unassigned      Down                  Down
GigabitEthernet0/7/0/12        unassigned      Down                  Down
GigabitEthernet0/7/0/13        unassigned      Down                  Down
GigabitEthernet0/7/0/14        unassigned      Down                  Down
GigabitEthernet0/7/0/15        unassigned      Up                    Up
GigabitEthernet0/7/0/16        unassigned      Down                  Down
GigabitEthernet0/7/0/17        unassigned      Down                  Down
GigabitEthernet0/7/0/18        unassigned      Down                  Down
GigabitEthernet0/7/0/19        unassigned      Down                  Down
GigabitEthernet0/7/0/20        unassigned      Down                  Down
GigabitEthernet0/7/0/21        unassigned      Down                  Down
GigabitEthernet0/7/0/22        unassigned      Down                  Down
GigabitEthernet0/7/0/23        unassigned      Down                  Down
GigabitEthernet0/7/0/24        unassigned      Down                  Down
GigabitEthernet0/7/0/25        unassigned      Down                  Down
GigabitEthernet0/7/0/26        unassigned      Down                  Down
GigabitEthernet0/7/0/27        unassigned      Down                  Down
GigabitEthernet0/7/0/28        unassigned      Down                  Down
GigabitEthernet0/7/0/29        unassigned      Down                  Down
GigabitEthernet0/7/0/30        unassigned      Down                  Down
GigabitEthernet0/7/0/31        unassigned      Down                  Down
GigabitEthernet0/7/0/32        unassigned      Down                  Down
GigabitEthernet0/7/0/33        unassigned      Down                  Down
GigabitEthernet0/7/0/34        unassigned      Down                  Down
GigabitEthernet0/7/0/35        unassigned      Down                  Down
GigabitEthernet0/7/0/36        unassigned      Down                  Down
GigabitEthernet0/7/0/37        unassigned      Down                  Down
GigabitEthernet0/7/0/38        unassigned      Down                  Down
GigabitEthernet0/7/0/39        unassigned      Down                  Down
>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down\n'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
Interface                      IP-Address      Status                Protocol

Loopback0                      51.51.51.51     Up                    Up

MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up

MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down

MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up

HundredGigE0/1/0/0             unassigned      Shutdown              Down

HundredGigE0/1/0/1             unassigned      Shutdown              Down

TenGigE0/2/0/0                 unassigned      Down                  Down

TenGigE0/2/0/1                 unassigned      Down                  Down

TenGigE0/2/0/2                 unassigned      Down                  Down

TenGigE0/2/0/4                 unassigned      Down                  Down

TenGigE0/2/0/5                 unassigned      Down                  Down

TenGigE0/2/0/6                 unassigned      Down                  Down

TenGigE0/2/0/7                 unassigned      Down                  Down

GigabitEthernet0/3/0/1         unassigned      Up                    Up

GigabitEthernet0/3/0/2         unassigned      Down                  Down

GigabitEthernet0/3/0/3         unassigned      Up                    Up

GigabitEthernet0/3/0/4         unassigned      Down                  Down

GigabitEthernet0/3/0/5         unassigned      Down                  Down

GigabitEthernet0/3/0/6         unassigned      Down                  Down

GigabitEthernet0/3/0/7         unassigned      Down                  Down

GigabitEthernet0/3/0/8         unassigned      Down                  Down

GigabitEthernet0/3/0/9         unassigned      Down                  Down

GigabitEthernet0/3/0/10        unassigned      Down                  Down

GigabitEthernet0/3/0/11        unassigned      Down                  Down

GigabitEthernet0/3/0/12        unassigned      Down                  Down

GigabitEthernet0/3/0/13        unassigned      Down                  Down

GigabitEthernet0/3/0/14        unassigned      Down                  Down

GigabitEthernet0/3/0/15        unassigned      Down                  Down

GigabitEthernet0/3/0/16        unassigned      Down                  Down

GigabitEthernet0/3/0/17        unassigned      Down                  Down

GigabitEthernet0/3/0/18        unassigned      Down                  Down

GigabitEthernet0/3/0/19        unassigned      Down                  Down

TenGigE0/3/1/0                 unassigned      Up                    Up

TenGigE0/3/1/1                 unassigned      Down                  Down

TenGigE0/3/1/2                 unassigned      Down                  Down

TenGigE0/3/1/3                 unassigned      Up                    Up

GigabitEthernet0/4/0/0         unassigned      Down                  Down

TenGigE0/4/0/0                 unassigned      Up                    Up

GigabitEthernet0/4/0/1         unassigned      Down                  Down

TenGigE0/4/0/1                 unassigned      Down                  Down

GigabitEthernet0/4/0/2         unassigned      Down                  Down

GigabitEthernet0/4/0/3         unassigned      Down                  Down

GigabitEthernet0/4/0/4         unassigned      Down                  Down

GigabitEthernet0/4/0/5         unassigned      Down                  Down

GigabitEthernet0/4/0/6         unassigned      Down                  Down

GigabitEthernet0/4/0/7         unassigned      Down                  Down

GigabitEthernet0/4/0/8         unassigned      Down                  Down

GigabitEthernet0/4/0/9         unassigned      Down                  Down

GigabitEthernet0/4/0/10        unassigned      Down                  Down

GigabitEthernet0/4/0/11        unassigned      Down                  Down

GigabitEthernet0/4/0/12        unassigned      Down                  Down

GigabitEthernet0/4/0/13        unassigned      Down                  Down

GigabitEthernet0/4/0/14        unassigned      Down                  Down

GigabitEthernet0/4/0/15        unassigned      Down                  Down

GigabitEthernet0/4/0/16        unassigned      Down                  Down

GigabitEthernet0/4/0/17        unassigned      Down                  Down

GigabitEthernet0/4/0/18        unassigned      Down                  Down

GigabitEthernet0/4/0/19        unassigned      Down                  Down

FortyGigE0/5/0/0               unassigned      Shutdown              Down

FortyGigE0/5/0/1               unassigned      Shutdown              Down

TenGigE0/5/1/0                 unassigned      Shutdown              Down

TenGigE0/5/1/1                 111.1.1.1       Up                    Up

GigabitEthernet0/7/0/0         unassigned      Down                  Down

GigabitEthernet0/7/0/1         unassigned      Down                  Down

GigabitEthernet0/7/0/2         unassigned      Down                  Down

GigabitEthernet0/7/0/3         unassigned      Down                  Down

GigabitEthernet0/7/0/4         unassigned      Down                  Down

GigabitEthernet0/7/0/5         unassigned      Down                  Down

GigabitEthernet0/7/0/6         unassigned      Down                  Down

GigabitEthernet0/7/0/7         unassigned      Down                  Down

GigabitEthernet0/7/0/8         unassigned      Down                  Down

GigabitEthernet0/7/0/9         unassigned      Down                  Down

GigabitEthernet0/7/0/10        unassigned      Down                  Down

GigabitEthernet0/7/0/11        unassigned      Down                  Down

GigabitEthernet0/7/0/12        unassigned      Down                  Down

GigabitEthernet0/7/0/13        unassigned      Down                  Down

GigabitEthernet0/7/0/14        unassigned      Down                  Down

GigabitEthernet0/7/0/15        unassigned      Up                    Up

GigabitEthernet0/7/0/16        unassigned      Down                  Down

GigabitEthernet0/7/0/17        unassigned      Down                  Down

GigabitEthernet0/7/0/18        unassigned      Down                  Down

GigabitEthernet0/7/0/19        unassigned      Down                  Down

GigabitEthernet0/7/0/20        unassigned      Down                  Down

GigabitEthernet0/7/0/21        unassigned      Down                  Down

GigabitEthernet0/7/0/22        unassigned      Down                  Down

GigabitEthernet0/7/0/23        unassigned      Down                  Down

GigabitEthernet0/7/0/24        unassigned      Down                  Down

GigabitEthernet0/7/0/25        unassigned      Down                  Down

GigabitEthernet0/7/0/26        unassigned      Down                  Down

GigabitEthernet0/7/0/27        unassigned      Down                  Down

GigabitEthernet0/7/0/28        unassigned      Down                  Down

GigabitEthernet0/7/0/29        unassigned      Down                  Down

GigabitEthernet0/7/0/30        unassigned      Down                  Down

GigabitEthernet0/7/0/31        unassigned      Down                  Down

GigabitEthernet0/7/0/32        unassigned      Down                  Down

GigabitEthernet0/7/0/33        unassigned      Down                  Down

GigabitEthernet0/7/0/34        unassigned      Down                  Down

GigabitEthernet0/7/0/35        unassigned      Down                  Down

GigabitEthernet0/7/0/36        unassigned      Down                  Down

GigabitEthernet0/7/0/37        unassigned      Down                  Down

GigabitEthernet0/7/0/38        unassigned      Down                  Down

GigabitEthernet0/7/0/39        unassigned      Down                  Down

>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down\n'
>>> line.rstrip()
'GigabitEthernet0/7/0/39        unassigned      Down                  Down'
>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down\n'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
Interface                      IP-Address      Status                Protocol
Loopback0                      51.51.51.51     Up                    Up
MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up
MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down
MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up
HundredGigE0/1/0/0             unassigned      Shutdown              Down
HundredGigE0/1/0/1             unassigned      Shutdown              Down
TenGigE0/2/0/0                 unassigned      Down                  Down
TenGigE0/2/0/1                 unassigned      Down                  Down
TenGigE0/2/0/2                 unassigned      Down                  Down
TenGigE0/2/0/4                 unassigned      Down                  Down
TenGigE0/2/0/5                 unassigned      Down                  Down
TenGigE0/2/0/6                 unassigned      Down                  Down
TenGigE0/2/0/7                 unassigned      Down                  Down
GigabitEthernet0/3/0/1         unassigned      Up                    Up
GigabitEthernet0/3/0/2         unassigned      Down                  Down
GigabitEthernet0/3/0/3         unassigned      Up                    Up
GigabitEthernet0/3/0/4         unassigned      Down                  Down
GigabitEthernet0/3/0/5         unassigned      Down                  Down
GigabitEthernet0/3/0/6         unassigned      Down                  Down
GigabitEthernet0/3/0/7         unassigned      Down                  Down
GigabitEthernet0/3/0/8         unassigned      Down                  Down
GigabitEthernet0/3/0/9         unassigned      Down                  Down
GigabitEthernet0/3/0/10        unassigned      Down                  Down
GigabitEthernet0/3/0/11        unassigned      Down                  Down
GigabitEthernet0/3/0/12        unassigned      Down                  Down
GigabitEthernet0/3/0/13        unassigned      Down                  Down
GigabitEthernet0/3/0/14        unassigned      Down                  Down
GigabitEthernet0/3/0/15        unassigned      Down                  Down
GigabitEthernet0/3/0/16        unassigned      Down                  Down
GigabitEthernet0/3/0/17        unassigned      Down                  Down
GigabitEthernet0/3/0/18        unassigned      Down                  Down
GigabitEthernet0/3/0/19        unassigned      Down                  Down
TenGigE0/3/1/0                 unassigned      Up                    Up
TenGigE0/3/1/1                 unassigned      Down                  Down
TenGigE0/3/1/2                 unassigned      Down                  Down
TenGigE0/3/1/3                 unassigned      Up                    Up
GigabitEthernet0/4/0/0         unassigned      Down                  Down
TenGigE0/4/0/0                 unassigned      Up                    Up
GigabitEthernet0/4/0/1         unassigned      Down                  Down
TenGigE0/4/0/1                 unassigned      Down                  Down
GigabitEthernet0/4/0/2         unassigned      Down                  Down
GigabitEthernet0/4/0/3         unassigned      Down                  Down
GigabitEthernet0/4/0/4         unassigned      Down                  Down
GigabitEthernet0/4/0/5         unassigned      Down                  Down
GigabitEthernet0/4/0/6         unassigned      Down                  Down
GigabitEthernet0/4/0/7         unassigned      Down                  Down
GigabitEthernet0/4/0/8         unassigned      Down                  Down
GigabitEthernet0/4/0/9         unassigned      Down                  Down
GigabitEthernet0/4/0/10        unassigned      Down                  Down
GigabitEthernet0/4/0/11        unassigned      Down                  Down
GigabitEthernet0/4/0/12        unassigned      Down                  Down
GigabitEthernet0/4/0/13        unassigned      Down                  Down
GigabitEthernet0/4/0/14        unassigned      Down                  Down
GigabitEthernet0/4/0/15        unassigned      Down                  Down
GigabitEthernet0/4/0/16        unassigned      Down                  Down
GigabitEthernet0/4/0/17        unassigned      Down                  Down
GigabitEthernet0/4/0/18        unassigned      Down                  Down
GigabitEthernet0/4/0/19        unassigned      Down                  Down
FortyGigE0/5/0/0               unassigned      Shutdown              Down
FortyGigE0/5/0/1               unassigned      Shutdown              Down
TenGigE0/5/1/0                 unassigned      Shutdown              Down
TenGigE0/5/1/1                 111.1.1.1       Up                    Up
GigabitEthernet0/7/0/0         unassigned      Down                  Down
GigabitEthernet0/7/0/1         unassigned      Down                  Down
GigabitEthernet0/7/0/2         unassigned      Down                  Down
GigabitEthernet0/7/0/3         unassigned      Down                  Down
GigabitEthernet0/7/0/4         unassigned      Down                  Down
GigabitEthernet0/7/0/5         unassigned      Down                  Down
GigabitEthernet0/7/0/6         unassigned      Down                  Down
GigabitEthernet0/7/0/7         unassigned      Down                  Down
GigabitEthernet0/7/0/8         unassigned      Down                  Down
GigabitEthernet0/7/0/9         unassigned      Down                  Down
GigabitEthernet0/7/0/10        unassigned      Down                  Down
GigabitEthernet0/7/0/11        unassigned      Down                  Down
GigabitEthernet0/7/0/12        unassigned      Down                  Down
GigabitEthernet0/7/0/13        unassigned      Down                  Down
GigabitEthernet0/7/0/14        unassigned      Down                  Down
GigabitEthernet0/7/0/15        unassigned      Up                    Up
GigabitEthernet0/7/0/16        unassigned      Down                  Down
GigabitEthernet0/7/0/17        unassigned      Down                  Down
GigabitEthernet0/7/0/18        unassigned      Down                  Down
GigabitEthernet0/7/0/19        unassigned      Down                  Down
GigabitEthernet0/7/0/20        unassigned      Down                  Down
GigabitEthernet0/7/0/21        unassigned      Down                  Down
GigabitEthernet0/7/0/22        unassigned      Down                  Down
GigabitEthernet0/7/0/23        unassigned      Down                  Down
GigabitEthernet0/7/0/24        unassigned      Down                  Down
GigabitEthernet0/7/0/25        unassigned      Down                  Down
GigabitEthernet0/7/0/26        unassigned      Down                  Down
GigabitEthernet0/7/0/27        unassigned      Down                  Down
GigabitEthernet0/7/0/28        unassigned      Down                  Down
GigabitEthernet0/7/0/29        unassigned      Down                  Down
GigabitEthernet0/7/0/30        unassigned      Down                  Down
GigabitEthernet0/7/0/31        unassigned      Down                  Down
GigabitEthernet0/7/0/32        unassigned      Down                  Down
GigabitEthernet0/7/0/33        unassigned      Down                  Down
GigabitEthernet0/7/0/34        unassigned      Down                  Down
GigabitEthernet0/7/0/35        unassigned      Down                  Down
GigabitEthernet0/7/0/36        unassigned      Down                  Down
GigabitEthernet0/7/0/37        unassigned      Down                  Down
GigabitEthernet0/7/0/38        unassigned      Down                  Down
GigabitEthernet0/7/0/39        unassigned      Down                  Down
>>> 
>>> 
>>> 
>>> line
'GigabitEthernet0/7/0/39        unassigned      Down                  Down'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
['Interface', 'IP-Address', 'Status', 'Protocol']
['Loopback0', '51.51.51.51', 'Up', 'Up']
['MgmtEth0/RSP0/CPU0/0', '1.20.30.40', 'Up', 'Up']
['MgmtEth0/RSP0/CPU0/1', 'unassigned', 'Down', 'Down']
['MgmtEth0/RSP1/CPU0/0', 'unassigned', 'Up', 'Up']
['HundredGigE0/1/0/0', 'unassigned', 'Shutdown', 'Down']
['HundredGigE0/1/0/1', 'unassigned', 'Shutdown', 'Down']
['TenGigE0/2/0/0', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/1', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/2', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/4', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/5', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/6', 'unassigned', 'Down', 'Down']
['TenGigE0/2/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/1', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/3/0/2', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/3', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/3/0/4', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/5', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/6', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/8', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/9', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/10', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/11', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/12', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/13', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/14', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/15', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/16', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/17', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/18', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/3/0/19', 'unassigned', 'Down', 'Down']
['TenGigE0/3/1/0', 'unassigned', 'Up', 'Up']
['TenGigE0/3/1/1', 'unassigned', 'Down', 'Down']
['TenGigE0/3/1/2', 'unassigned', 'Down', 'Down']
['TenGigE0/3/1/3', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/4/0/0', 'unassigned', 'Down', 'Down']
['TenGigE0/4/0/0', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/4/0/1', 'unassigned', 'Down', 'Down']
['TenGigE0/4/0/1', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/2', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/3', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/4', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/5', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/6', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/8', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/9', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/10', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/11', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/12', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/13', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/14', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/15', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/16', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/17', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/18', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/4/0/19', 'unassigned', 'Down', 'Down']
['FortyGigE0/5/0/0', 'unassigned', 'Shutdown', 'Down']
['FortyGigE0/5/0/1', 'unassigned', 'Shutdown', 'Down']
['TenGigE0/5/1/0', 'unassigned', 'Shutdown', 'Down']
['TenGigE0/5/1/1', '111.1.1.1', 'Up', 'Up']
['GigabitEthernet0/7/0/0', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/1', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/2', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/3', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/4', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/5', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/6', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/7', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/8', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/9', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/10', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/11', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/12', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/13', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/14', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/15', 'unassigned', 'Up', 'Up']
['GigabitEthernet0/7/0/16', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/17', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/18', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/19', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/20', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/21', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/22', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/23', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/24', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/25', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/26', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/27', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/28', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/29', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/30', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/31', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/32', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/33', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/34', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/35', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/36', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/37', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/38', 'unassigned', 'Down', 'Down']
['GigabitEthernet0/7/0/39', 'unassigned', 'Down', 'Down']
>>> len(fields)
4
>>> fields[0]
'GigabitEthernet0/7/0/39'
>>> fields[-1]
'Down'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
IP-Address Interface
51.51.51.51 Loopback0
1.20.30.40 MgmtEth0/RSP0/CPU0/0
unassigned MgmtEth0/RSP0/CPU0/1
unassigned MgmtEth0/RSP1/CPU0/0
unassigned HundredGigE0/1/0/0
unassigned HundredGigE0/1/0/1
unassigned TenGigE0/2/0/0
unassigned TenGigE0/2/0/1
unassigned TenGigE0/2/0/2
unassigned TenGigE0/2/0/4
unassigned TenGigE0/2/0/5
unassigned TenGigE0/2/0/6
unassigned TenGigE0/2/0/7
unassigned GigabitEthernet0/3/0/1
unassigned GigabitEthernet0/3/0/2
unassigned GigabitEthernet0/3/0/3
unassigned GigabitEthernet0/3/0/4
unassigned GigabitEthernet0/3/0/5
unassigned GigabitEthernet0/3/0/6
unassigned GigabitEthernet0/3/0/7
unassigned GigabitEthernet0/3/0/8
unassigned GigabitEthernet0/3/0/9
unassigned GigabitEthernet0/3/0/10
unassigned GigabitEthernet0/3/0/11
unassigned GigabitEthernet0/3/0/12
unassigned GigabitEthernet0/3/0/13
unassigned GigabitEthernet0/3/0/14
unassigned GigabitEthernet0/3/0/15
unassigned GigabitEthernet0/3/0/16
unassigned GigabitEthernet0/3/0/17
unassigned GigabitEthernet0/3/0/18
unassigned GigabitEthernet0/3/0/19
unassigned TenGigE0/3/1/0
unassigned TenGigE0/3/1/1
unassigned TenGigE0/3/1/2
unassigned TenGigE0/3/1/3
unassigned GigabitEthernet0/4/0/0
unassigned TenGigE0/4/0/0
unassigned GigabitEthernet0/4/0/1
unassigned TenGigE0/4/0/1
unassigned GigabitEthernet0/4/0/2
unassigned GigabitEthernet0/4/0/3
unassigned GigabitEthernet0/4/0/4
unassigned GigabitEthernet0/4/0/5
unassigned GigabitEthernet0/4/0/6
unassigned GigabitEthernet0/4/0/7
unassigned GigabitEthernet0/4/0/8
unassigned GigabitEthernet0/4/0/9
unassigned GigabitEthernet0/4/0/10
unassigned GigabitEthernet0/4/0/11
unassigned GigabitEthernet0/4/0/12
unassigned GigabitEthernet0/4/0/13
unassigned GigabitEthernet0/4/0/14
unassigned GigabitEthernet0/4/0/15
unassigned GigabitEthernet0/4/0/16
unassigned GigabitEthernet0/4/0/17
unassigned GigabitEthernet0/4/0/18
unassigned GigabitEthernet0/4/0/19
unassigned FortyGigE0/5/0/0
unassigned FortyGigE0/5/0/1
unassigned TenGigE0/5/1/0
111.1.1.1 TenGigE0/5/1/1
unassigned GigabitEthernet0/7/0/0
unassigned GigabitEthernet0/7/0/1
unassigned GigabitEthernet0/7/0/2
unassigned GigabitEthernet0/7/0/3
unassigned GigabitEthernet0/7/0/4
unassigned GigabitEthernet0/7/0/5
unassigned GigabitEthernet0/7/0/6
unassigned GigabitEthernet0/7/0/7
unassigned GigabitEthernet0/7/0/8
unassigned GigabitEthernet0/7/0/9
unassigned GigabitEthernet0/7/0/10
unassigned GigabitEthernet0/7/0/11
unassigned GigabitEthernet0/7/0/12
unassigned GigabitEthernet0/7/0/13
unassigned GigabitEthernet0/7/0/14
unassigned GigabitEthernet0/7/0/15
unassigned GigabitEthernet0/7/0/16
unassigned GigabitEthernet0/7/0/17
unassigned GigabitEthernet0/7/0/18
unassigned GigabitEthernet0/7/0/19
unassigned GigabitEthernet0/7/0/20
unassigned GigabitEthernet0/7/0/21
unassigned GigabitEthernet0/7/0/22
unassigned GigabitEthernet0/7/0/23
unassigned GigabitEthernet0/7/0/24
unassigned GigabitEthernet0/7/0/25
unassigned GigabitEthernet0/7/0/26
unassigned GigabitEthernet0/7/0/27
unassigned GigabitEthernet0/7/0/28
unassigned GigabitEthernet0/7/0/29
unassigned GigabitEthernet0/7/0/30
unassigned GigabitEthernet0/7/0/31
unassigned GigabitEthernet0/7/0/32
unassigned GigabitEthernet0/7/0/33
unassigned GigabitEthernet0/7/0/34
unassigned GigabitEthernet0/7/0/35
unassigned GigabitEthernet0/7/0/36
unassigned GigabitEthernet0/7/0/37
unassigned GigabitEthernet0/7/0/38
unassigned GigabitEthernet0/7/0/39
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51 Loopback0
1.20.30.40 MgmtEth0/RSP0/CPU0/0
unassigned MgmtEth0/RSP1/CPU0/0
unassigned GigabitEthernet0/3/0/1
unassigned GigabitEthernet0/3/0/3
unassigned TenGigE0/3/1/0
unassigned TenGigE0/3/1/3
unassigned TenGigE0/4/0/0
111.1.1.1 TenGigE0/5/1/1
unassigned GigabitEthernet0/7/0/15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet0/7/0/15
>>> len('255.255.255.255')
15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51                    Loopback0
1.20.30.40                     MgmtEth0/RSP0/CPU0/0
unassigned                     MgmtEth0/RSP1/CPU0/0
unassigned                     GigabitEthernet0/3/0/1
unassigned                     GigabitEthernet0/3/0/3
unassigned                     TenGigE0/3/1/0
unassigned                     TenGigE0/3/1/3
unassigned                     TenGigE0/4/0/0
111.1.1.1                      TenGigE0/5/1/1
unassigned                     GigabitEthernet0/7/0/15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet0/7/0/15
>>> len('255.255.255.255')
15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51    , Loopback0
1.20.30.40     , MgmtEth0/RSP0/CPU0/0
unassigned     , MgmtEth0/RSP1/CPU0/0
unassigned     , GigabitEthernet0/3/0/1
unassigned     , GigabitEthernet0/3/0/3
unassigned     , TenGigE0/3/1/0
unassigned     , TenGigE0/3/1/3
unassigned     , TenGigE0/4/0/0
111.1.1.1      , TenGigE0/5/1/1
unassigned     , GigabitEthernet0/7/0/15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet0/7/0/15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet0/7/0/15
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/show_ipv4.py", line 13, in <module>
    interface, ipaddr, status, protocol = line.split()
ValueError: not enough values to unpack (expected 4, got 3)
>>> line
'GigabitEthernet0/7/0/38        unassigned                            Down'
>>> line.split()
['GigabitEthernet0/7/0/38', 'unassigned', 'Down']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet0/7/0/15
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj164/show_ipv4.py", line 14, in <module>
    interface, ipaddr, status, protocol = line.split()
ValueError: too many values to unpack (expected 4)
>>> line
'Gigabit Ethernet 0/7/0/28      unassigned      Down                  Down'
>>> line.split()
['Gigabit', 'Ethernet', '0/7/0/28', 'unassigned', 'Down', 'Down']
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
>>> line
'GigabitEthernet0/7/0/39      unassigned      Down               Down\n'
>>> interface
'GigabitEthernet0/7/0/39      un'
>>> ipaddr
'assigned      Do'
>>> status
'wn               Down'
>>> protocol
''
>>> s = [10, 20, 30]
>>> for x in s:
	print(x, x**2)

	
10 100
20 400
30 900
>>> 
>>> it = iter(s)
>>> x = next(it)
>>> print(x, x**2)
10 100
>>> x = next(it)
>>> print(x, x**2)
20 400
>>> x = next(it)
>>> print(x, x**2)
30 900
>>> x = next(it)
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    x = next(it)
StopIteration
>>> s = [10, 20, 30]
>>> it = iter(s)
>>> next(s)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    next(s)
TypeError: 'list' object is not an iterator
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s = [10, 20, 30]
>>> it = iter(s)
>>> next(it)
10
>>> for x in s:
	print(x, x**2)

	
10 100
20 400
30 900
>>> for x in it:
	print(x, x**2)

	
20 400
30 900
>>> 
>>> 
>>> f = open('notestdd/stocks.txt')
>>> next(f)
'CSCO,100,18.04\n'
>>> for line in f:
	print(line, sep='')

	
ANTM,200,45.03

CSCO,150,19.05

MSFT,250,80.56

IBM,500,22.01

ANTM,250,44.23

GOOG,200,501.45

CSCO,175,19.56

MSFT,75,80.81

GOOG,300,502.65

IBM,150,25.01

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
This is the header: Interface                    IP-Address      Status             Protocol

>>> header
'Interface                    IP-Address      Status             Protocol\n'
>>> header.startswith('Interface')
True
>>> 
>>> header
'Interface                    IP-Address      Status             Protocol\n'
>>> header.find('Interface')
0
>>> header.find('IP-Address')
29
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/show_ipv4.py =========
51.51.51.51     Loopback0
1.20.30.40      MgmtEth0/RSP0/CPU0/0
unassigned      MgmtEth0/RSP1/CPU0/0
unassigned      GigabitEthernet0/3/0/1
unassigned      GigabitEthernet0/3/0/3
unassigned      TenGigE0/3/1/0
unassigned      TenGigE0/3/1/3
unassigned      TenGigE0/4/0/0
111.1.1.1       TenGigE0/5/1/1
unassigned      GigabitEthernet 0/7/0/15
>>> 
>>> 
>>> s = '42'
>>> int(s)
42
>>> n = 42
>>> str(42)
'42'
>>> person = ('raymond', 'hettinger', 0x35, 'python@rcn.com')
>>> fname, lname, age, email = person
>>> 
>>> s = []
>>> for i in range(5):
	sqr = i ** 2
	s.append(sqr)

	
>>> s
[0, 1, 4, 9, 16]
>>> # See vcard.py for an example
>>> # Test as you go.  Looking at the results.
>>> # Get code working first, line by line,
>>> # perhaps hardwired to specific values.
>>> # Once it works, move into a function and parameterize.
>>> # Put test code in a __main__ section
>>> # Module starts with a module doctring, then imports,
>>> # then function definitions, then main section and tests.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/portfolio.py =========
('CSCO', '100', '18.04')
('ANTM', '200', '45.03')
('CSCO', '150', '19.05')
('MSFT', '250', '80.56')
('IBM', '500', '22.01')
('ANTM', '250', '44.23')
('GOOG', '200', '501.45')
('CSCO', '175', '19.56')
('MSFT', '75', '80.81')
('GOOG', '300', '502.65')
('IBM', '150', '25.01')
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/portfolio.py =========
('CSCO', 100, 18.04)
('ANTM', 200, 45.03)
('CSCO', 150, 19.05)
('MSFT', 250, 80.56)
('IBM', 500, 22.01)
('ANTM', 250, 44.23)
('GOOG', 200, 501.45)
('CSCO', 175, 19.56)
('MSFT', 75, 80.81)
('GOOG', 300, 502.65)
('IBM', 150, 25.01)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/portfolio.py =========
[('CSCO', 100, 18.04), ('ANTM', 200, 45.03), ('CSCO', 150, 19.05), ('MSFT', 250, 80.56), ('IBM', 500, 22.01), ('ANTM', 250, 44.23), ('GOOG', 200, 501.45), ('CSCO', 175, 19.56), ('MSFT', 75, 80.81), ('GOOG', 300, 502.65), ('IBM', 150, 25.01)]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/portfolio.py =========
[('CSCO', 100, 18.04), ('ANTM', 200, 45.03), ('CSCO', 150, 19.05), ('MSFT', 250, 80.56), ('IBM', 500, 22.01), ('ANTM', 250, 44.23), ('GOOG', 200, 501.45), ('CSCO', 175, 19.56), ('MSFT', 75, 80.81), ('GOOG', 300, 502.65), ('IBM', 150, 25.01)]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/portfolio.py =========
[('CSCO', 100, 18.04), ('ANTM', 200, 45.03), ('CSCO', 150, 19.05), ('MSFT', 250, 80.56), ('IBM', 500, 22.01), ('ANTM', 250, 44.23), ('GOOG', 200, 501.45), ('CSCO', 175, 19.56), ('MSFT', 75, 80.81), ('GOOG', 300, 502.65), ('IBM', 150, 25.01)]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj164/portfolio.py =========
[('CSCO', 100, 18.04), ('ANTM', 200, 45.03), ('CSCO', 150, 19.05), ('MSFT', 250, 80.56), ('IBM', 500, 22.01), ('ANTM', 250, 44.23), ('GOOG', 200, 501.45), ('CSCO', 175, 19.56), ('MSFT', 75, 80.81), ('GOOG', 300, 502.65), ('IBM', 150, 25.01)]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # Old-way
>>> n = 10
>>> squares = []
>>> for i in range(n):
	s = i ** 2
	squares.append(s)

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> sum(squares)
285
>>> [i**2 for i in range(n)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> sum([i**2 for i in range(n)])
285
>>> len([i**2 for i in range(n)])
10
>>> min([i**2 for i in range(n)])
0
>>> max([i**2 for i in range(n)])
81
>>> [i**2 for i in range(n) if x%2==0]
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    [i**2 for i in range(n) if x%2==0]
  File "<pyshell#274>", line 1, in <listcomp>
    [i**2 for i in range(n) if x%2==0]
NameError: name 'x' is not defined
>>> [x**2 for x in range(n) if x%2==0]
[0, 4, 16, 36, 64]
>>> 
>>> 
>>> 
>>> 
>>> n = 10
>>> [x**2 for x in range(n) if x%2==0]
[0, 4, 16, 36, 64]
>>> # LC are good math!
>>> names = 'manny mo jack'.split()
>>> names
['manny', 'mo', 'jack']
>>> [name.capitalize() for name in names]
['Manny', 'Mo', 'Jack']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> [name.capitalize() for name in names if name.startswith('m')]
['Manny', 'Mo']
>>> # LC are good at string processing
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> chr(97)
'a'
>>> ord('A')
65
>>> ord('B')
66
>>> ord('a')
97
>>> [ord(c) for c in 'Raymond']
[82, 97, 121, 109, 111, 110, 100]
>>> [ord(c) + 13 for c in 'Raymond']
[95, 110, 134, 122, 124, 123, 113]
>>> [chr(ord(c) + 13) for c in 'Raymond']
['_', 'n', '\x86', 'z', '|', '{', 'q']
>>> code = ''.join([chr(ord(c) + 13) for c in 'Raymond'])
>>> code
'_n\x86z|{q'
>>> ''.join([chr(ord(c) - 13) for c in code])
'Raymond'
>>> # LC are good at light-weight crypto
>>> 
>>> ll = [len(line) for line in open('notestdd/stocks.txt')]
>>> ll
[15, 15, 15, 15, 14, 15, 16, 15, 14, 16, 14]
>>> len(ll)
11
>>> sum(ll)
164
>>> min(ll)
14
>>> max(ll)
16
>>> # LC are have WC-like capabilities
>>> [line for line in open('notestdd/stocks.txt') if 'CSCO' in line]
['CSCO,100,18.04\n', 'CSCO,150,19.05\n', 'CSCO,175,19.56\n']
>>> print(''.join([line for line in open('notestdd/stocks.txt') if 'CSCO' in line]))
CSCO,100,18.04
CSCO,150,19.05
CSCO,175,19.56

>>> # LC are have GREP-like capabilities
>>> [line for line in open('notestdd/stocks.txt') if 'CSCO' in line]
['CSCO,100,18.04\n', 'CSCO,150,19.05\n', 'CSCO,175,19.56\n']
>>> [line.split(',') for line in open('notestdd/stocks.txt') if 'CSCO' in line]
[['CSCO', '100', '18.04\n'], ['CSCO', '150', '19.05\n'], ['CSCO', '175', '19.56\n']]
>>> [line.split(',')[0] for line in open('notestdd/stocks.txt') if 'CSCO' in line]
['CSCO', 'CSCO', 'CSCO']
>>> [line.split(',')[1] for line in open('notestdd/stocks.txt') if 'CSCO' in line]
['100', '150', '175']
>>> [int(line.split(',')[1]) for line in open('notestdd/stocks.txt') if 'CSCO' in line]
[100, 150, 175]
>>> sum([int(line.split(',')[1]) for line in open('notestdd/stocks.txt') if 'CSCO' in line])
425
>>> # awk 'BEGIN { FS  = ","} /CSCO/ { total += $2 } END { print total }' notestdd/stocks.txt
>>> # LC are have AWK-like capabilities
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj164/download.py ==========
======================== Source: https://dl.dropboxusercontent.com/u/3967849/sj164/links.txt ========================
                                    Starting download at Thu Jul 13 16:26:09 2017                                    
200* OK               https://dl.dropbox.com/u/3967849/shared/call_by_object.txt --> notestdd/call_by_object.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/sj164/links.txt        --> notestdd/links.txt        (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/log_parse_demo.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/welcome.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/download.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/how_dunder_name_works.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/test_minimum.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/the_minimum.py
200* OK               https://dl.dropbox.com/u/3967849/sj164/basics.log       --> notestdd/basics.log       (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/basics.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/dict_overview.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/test_the_minimum_with_beck_framework.py
200* OK               https://dl.dropbox.com/u/3967849/sj164/tdd_from_scratch.log --> notestdd/tdd_from_scratch.log (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/buggy_math_module.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/test_math_package_with_hypothesis.py
200* OK               https://dl.dropbox.com/u/3967849/sj164/the_min_tests.log --> notestdd/the_min_tests.log (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/test_math_package_with_coverage.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/magic_methods.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/test_beck.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/beck.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/vcard.py
200* OK               https://dl.dropbox.com/u/3967849/sj164/raisins.log      --> notestdd/raisins.log      (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/test_dict.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/dictionary.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/github_rest_api.py
404  Not Found        https://dl.dropbox.com/u/3967849/sj164/test_minimum_pytest_style
200* OK               https://dl.dropbox.com/u/3967849/sj164/test_dict.py,cover --> notestdd/test_dict.py,cover (current) 
200* OK               https://dl.dropbox.com/u/3967849/sj164/dictionary.py,cover --> notestdd/dictionary.py,cover (current) 
200* OK               https://dl.dropbox.com/u/3967849/sj164/beck.py,cover    --> notestdd/beck.py,cover    (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/show_ipv4.py
200  OK               https://dl.dropbox.com/u/3967849/sj164/portfolio.py     --> notestdd/portfolio.py     (updated) 
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
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/day1.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/day2.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj164/day3.py
200  OK               https://dl.dropbox.com/u/3967849/sj164/day4.py          --> notestdd/day4.py          (updated) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/__init__.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/bottle.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/CSRRESTAPI.pdf
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/Polya_HowToSolveIt.pdf
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/Raymond_Hettinger.png
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/Raymond_Hettinger.vcf
200* OK               https://dl.dropbox.com/u/3967849/shared/books.json      --> notestdd/books.json       (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/books.xml       --> notestdd/books.xml        (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/crossword_challenge.py
200* OK               https://dl.dropbox.com/u/3967849/shared/dns_servers.json --> notestdd/dns_servers.json (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/email.txt       --> notestdd/email.txt        (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/english_composition.txt --> notestdd/english_composition.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/family_template.txt --> notestdd/family_template.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/fruit.xml       --> notestdd/fruit.xml        (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/hamlet.txt      --> notestdd/hamlet.txt       (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/interfaces.xml  --> notestdd/interfaces.xml   (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/ipv4_int_bri.txt --> notestdd/ipv4_int_bri.txt (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/kap.dot
200* OK               https://dl.dropbox.com/u/3967849/shared/kap.svg         --> notestdd/kap.svg          (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/member_template.txt --> notestdd/member_template.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/nasa_19950801.log --> notestdd/nasa_19950801.log (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/oop_story.txt   --> notestdd/oop_story.txt    (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/parse_demo2.txt --> notestdd/parse_demo2.txt  (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/ping_output.txt --> notestdd/ping_output.txt  (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/queue_stats.txt --> notestdd/queue_stats.txt  (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/raisin_team.csv --> notestdd/raisin_team.csv  (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/raisin_team_update.csv --> notestdd/raisin_team_update.csv (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/re.txt          --> notestdd/re.txt           (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/rss.xml         --> notestdd/rss.xml          (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/show_controllers.txt --> notestdd/show_controllers.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/stocks.txt      --> notestdd/stocks.txt       (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/team_history.json --> notestdd/team_history.json (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/team_history.txt --> notestdd/team_history.txt (current) 
>>> 
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
Our team history:

* On 3/14/2013, we scored 14 points and lost the game.
* On 6/2/2013, we scored 15 points and lost the game.
* On 9/15/2013, we scored only 1 point and won the game.

Go figure!

>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
Our team history:

* On 3/14/2013, we scored 14 points and lost the game.
* On 6/2/2013, we scored 15 points and lost the game.
* On 9/15/2013, we scored only 1 point and won the game.

Go figure!

>>> re.findall(r'team', hist)
['team']
>>> re.findall(r'te.m', hist)
['team']
>>> re.findall(r'te..m', hist)
[]
>>> re.findall(r'we', hist)
['we', 'we', 'we']
>>> re.findall(r'me', hist)
['me', 'me', 'me']
>>> re.findall(r'\bwe\b', hist)
['we', 'we', 'we']
>>> re.findall(r'\bme\b', hist)
[]
>>> re.findall(r'[0-9]', hist)
['3', '1', '4', '2', '0', '1', '3', '1', '4', '6', '2', '2', '0', '1', '3', '1', '5', '9', '1', '5', '2', '0', '1', '3', '1']
>>> re.findall(r'[0-9]+', hist)
['3', '14', '2013', '14', '6', '2', '2013', '15', '9', '15', '2013', '1']
>>> re.findall(r'\d+', hist)
['3', '14', '2013', '14', '6', '2', '2013', '15', '9', '15', '2013', '1']
>>> re.findall(r'\d+ points', hist)
['14 points', '15 points']
>>> re.findall(r'\d+ point', hist)
['14 point', '15 point', '1 point']
>>> re.findall(r'(\d+) point', hist)
['14', '15', '1']
>>> [int(score) for score in re.findall(r'(\d+) point', hist)]
[14, 15, 1]
>>> scores = [int(score) for score in re.findall(r'(\d+) point', hist)]
>>> len(scores)
3
>>> scores[0]
14
>>> scores[-1]
1
>>> sum(scores)
30
>>> min(scores)
1
>>> max(scores)
15
>>> 
>>> re.findall(r'\d+', hist)
['3', '14', '2013', '14', '6', '2', '2013', '15', '9', '15', '2013', '1']
>>> re.findall(r'\d+/\d+/\d+', hist)
['3/14/2013', '6/2/2013', '9/15/2013']
>>> re.findall(r'[0-9]+/[0-9]+/[0-9]+', hist)
['3/14/2013', '6/2/2013', '9/15/2013']
>>> re.findall(r'[0-9]+/[0-9]+/[0-9]+', '123412341/2342345/123')
['123412341/2342345/123']
>>> re.findall(r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}', hist)
['3/14/2013', '6/2/2013', '9/15/2013']
>>> re.findall(r'won|lost', hist)
['lost', 'lost', 'won']
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
>>> scores
[14, 15, 1]
>>> dates
['3/14/2013', '6/2/2013', '9/15/2013']
>>> record
['lost', 'lost', 'won']
>>> record.count('lost')
2
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season from 3/14/2013 to 9/15/2013
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season from 3/14/2013 to 9/15/2013
We scored 30 goals this season
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season from 3/14/2013 to 9/15/2013
We scored 30 goals this season. Our worst was 1 and best was 15
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season from 3/14/2013 to 9/15/2013
We scored 30 goals this season. Our worst was 1 and best was 15
We lost the first game and won the last game
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season from 3/14/2013 to 9/15/2013
We scored 30 goals this season. Our worst was 1 and best was 15
We lost the first game and won the last game for a 0-0 record
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj164/show_team_history.py =====
We played 3 games this season from 3/14/2013 to 9/15/2013
We scored 30 goals this season. Our worst was 1 and best was 15
We lost the first game and won the last game for a 1-2 record
>>> 
>>> 
