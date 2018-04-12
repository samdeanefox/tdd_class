from dictionary import Dict
import pytest

def test_basics():
    d = Dict()
    d['grant'] = 'beer'
    d['peter'] = 'pinot grigio'
    d['nima'] = 'lemonade'
    d['raj'] = 'margarita'
    assert d['grant'] == 'beer'
    assert d['peter'] == 'pinot grigio'
    assert d['nima'] == 'lemonade'
    assert d['raj'] == 'margarita'

def test_key_not_found():
    d = Dict()
    with pytest.raises(KeyError):
        d['gerard']

if __name__ == '__main__':
    pytest.main(['test_dict.py'])