'Create a working dictionary from scratch'
# For more details of the actual Python implementation, see:
# https://www.youtube.com/watch?v=npw4s1QTmPg
# and http://bit.ly/pycon2017compdict

import time

_hashseed = int(time.time() * 101)

def myhash(s):
    'Deterministic string hash function'
    h = _hashseed
    for c in s:
        h = h * 17 + ord(c)
    return h

class Dict:
    'A custom dict reimplementation based on lists'

    def _get_desk_and_folder(self, key):
        i = myhash(key) % self.n
        desk = self.desks[i]
        folder = self.folders[i]
        return desk, folder

    def _find_position_at_a_desk(self, key, desk):
        try:
            return desk.index(key)
        except ValueError:
            raise KeyError(key)

    def __init__(self):                 # d = Dict()
        self.n = 8
        self.desks = [[] for i in range(self.n)]
        self.folders = [[] for i in range(self.n)]

    def __setitem__(self, key, value):  # d[k] = v
        if key in self:
            del self[key]
        desk, folder = self._get_desk_and_folder(key)
        desk.append(key)
        folder.append(value)

    def __getitem__(self, key):         # d[k]
        desk, folder = self._get_desk_and_folder(key)
        j = self._find_position_at_a_desk(key, desk)
        return folder[j]

    def __contains__(self, key):        # k in d
        try:
            self[key]
        except KeyError:
            return False
        return True

    def __delitem__(self, key):         # del d[k]
        desk, folder = self._get_desk_and_folder(key)
        j = self._find_position_at_a_desk(key, desk)
        del desk[j]
        del folder[j]

    def __len__(self):                  # len(d)
        return sum([len(desk) for desk in self.desks])

    def clear(self):                    # d.clear()
        for desk in self.desks:
            desk.clear()
        for folder in self.folders:
            folder.clear()

    def keys(self):
        result = []
        for desk in self.desks:
            for key in desk:
                result.append(key)
        return result

    def __repr__(self):
        pairs = ', '.join([f'{k!r}: {d[k]!r}' for k in self.keys()])
        return '{' + pairs + '}'


''' More todo:

    d.get(k, default)
    d.update(list_of_items())
    d.pop(k, default)
    d.setdefault()
    Variable size:  whenever the dict two-thirds full,
                    rebuild it will double the size

'''

