"""Test VCard Script

1. Convert CSV data to VCard format.
2. Convert VCard data to QR code image.
3. Parse the CSV file.

"""

import vcard
import pytest
import runpy
import beck
from unittest import mock

def test_make_vcard():
    text = vcard.make_vcard('Grant', 'Jenks', 'Raisin Janitor', 'grant@example.com', '555-555-5555')
    assert text.startswith('BEGIN:VCARD')
    assert 'Grant' in text

def test_make_vcard_jacky():
    text = vcard.make_vcard('Jacky', 'Smith', 'Raisin Taste Tester', 'jacky@example.com', '555-555-5555')
    assert text.startswith('BEGIN:VCARD')
    assert 'Jacky' in text

class TestQRCode():

    def test_make_qr_code(self):
        image = vcard.make_qr_code('I love Python')
        assert list(image[:8]) == [137, 80, 78, 71, 13, 10, 26, 10]

class FakeConnection:
    def read(self):
        return b'test image data'

    def close(self):
        pass

def fake_urlopen(url):
    return FakeConnection()

def test_make_qr_code_patched():
    with mock.patch('urllib.request.urlopen', fake_urlopen):
        image = vcard.make_qr_code('test data')
    assert image == b'test image data'

import runpy

class FakeFile:

    def __init__(self):
        self.writes = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        line = 'Hettinger,Raymond,VP Raisin Smushing,raymond@example.com'
        lines = [line]
        iterator = iter(lines)
        return iterator

    def write(self, data):
        self.writes.append(data)


def fake_open(filename, mode='r'):
    return FakeFile()

def test_script():
    fake_file = FakeFile()
    fake_open = lambda filename, mode='r': fake_file

    with mock.patch('urllib.request.urlopen', fake_urlopen):
        globs = {'open': fake_open}
        runpy.run_path('vcard.py', run_name='__main__')

    vcard_data, image_data = fake_file.writes
    assert vcard_data.startswith('BEGIN:VCARD')
    assert image_data == b'test image data'

if __name__ == '__main__':
    pytest.main(['-s', 'test_vcard.py'])