import beck
from dictionary import Dict, myhash

class TestDict(beck.TestCase):

    def test_basics(self):
        d = Dict()
        d['philip'] = 'white'
        d['rama'] = 'white'
        d['alejandro'] = 'blue'
        d['rucha'] = 'green'

    def test_myhash(self):
        assert isinstance(myhash('raymond'), int)
        assert myhash('raymond') == myhash('raymond')
        assert myhash('rachel') == myhash('rachel')
        assert myhash('raymond') != myhash('rachel')

    def test_lookup(self):
        d = Dict()
        d['philip'] = 'white'
        d['rama'] = 'white'
        d['alejandro'] = 'blue'
        assert d['philip'] == 'white'
        assert d['rama'] == 'white'
        assert d['alejandro'] == 'blue'
        with self.assert_raises(KeyError):
            d['craig']

    def test_membership(self):
        d = Dict()
        assert 'philip' not in d
        assert 'rama' not in d
        assert 'alejandro' not in d
        assert 'rucha' not in d
        assert 'tom' not in d
        d['philip'] = 'white'
        d['rama'] = 'white'
        d['alejandro'] = 'blue'
        d['rucha'] = 'green'
        assert 'philip' in d
        assert 'rama' in d
        assert 'alejandro' in d
        assert 'rucha' in d
        assert 'tom' not in d

    def test_deletion(self):
        d = Dict()
        d['philip'] = 'white'
        d['rama'] = 'white'
        d['alejandro'] = 'blue'
        d['rucha'] = 'green'
        assert 'philip' in d
        assert 'rama' in d
        assert 'alejandro' in d
        assert 'rucha' in d
        assert 'tom' not in d
        del d['philip']
        assert 'philip' not in d
        del d['rama']
        assert 'ram' not in d
        del d['alejandro']
        assert 'alejandro' not in d
        del d['rucha']
        assert 'rucha' not in d
        assert 'tom' not in d
        with self.assert_raises(KeyError):
            del d['tom']

    def test_len(self):
        d = Dict()
        assert len(d) == 0
        d['philip'] = 'white'
        assert len(d) == 1
        d['rama'] = 'white'
        assert len(d) == 2
        d['alejandro'] = 'blue'
        assert len(d) == 3
        d['rucha'] = 'green'
        assert len(d) == 4
        del d['philip']
        assert len(d) == 3
        del d['rama']
        assert len(d) == 2
        del d['alejandro']
        assert len(d) == 1
        del d['rucha']
        assert len(d) == 0

    def test_set_twice_bug(self):
        d = Dict()
        d['raymond'] = 'red'
        d['rachel'] = 'blue'
        d['rachel'] = 'azure'
        assert d['raymond'] == 'red'
        assert d['rachel'] == 'azure'
        assert len(d) == 2

    def test_myhash_reset_on_every_load(self):
        h = myhash('raymond')
        assert isinstance(h, int)
        h2 = myhash('raymond')
        assert h == h2
        # make sure h is not the same as myhash('raymond') gave on a previous runs
        assert h not in {62165369947073839459,
                         62165380346286829298,
                         62165387237104164987}

    def test_clear(self):
        d = Dict()
        d['philip'] = 'white'
        d['rama'] = 'white'
        d['alejandro'] = 'blue'
        d['rucha'] = 'green'
        assert len(d) == 4
        d.clear()
        assert len(d) == 0

    def test_keys(self):
        d = Dict()
        d['philip'] = 'white'
        d['rama'] = 'white'
        d['alejandro'] = 'blue'
        d['rucha'] = 'green'
        assert sorted(d.keys()) == sorted(['philip', 'rama', 'alejandro', 'rucha'])

if __name__ == '__main__':

    beck.run_tests(TestDict)
