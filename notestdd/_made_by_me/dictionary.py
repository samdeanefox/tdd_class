"""Create a working dictionary from scratch"""

class Dict:
    "Custom dictionary re-implementation of Python's built-n dict."

    def __init__(self):
        self.n = 8
        self.my_keys = []
        self.my_values = []
        for i in range(self.n):
            self.my_keys.append([])
            self.my_values.append([])

    def __getitem__(self, key):
        sublist_index = hash(key) % self.n
        sublist_keys = self.my_keys[sublist_index]
        sublist_values = self.my_values[sublist_index]
        try:
            position = self.my_keys.index(key)
            return sublist_values[position]
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        sublist_index = hash(key) % self.n
        sublist_keys = self.my_keys[sublist_index]
        sublist_values = self.my_values[sublist_index]
        if sublist_index in self.my_keys:
            position = self.my_keys.index(key)
            sublist_values[position] = value
        else:
            sublist_keys.append(key)
            sublist_values.append(value)

    def __delitem__(self, key):
        sublist_index = hash(key) % self.n
        sublist_keys = self.my_keys[sublist_index]
        sublist_values = self.my_values[sublist_index]
        if key in self.my_keys:
            position = sublist_keys.index(key)
            del sublist_keys[position]
            del sublist_values[position]
        else:
            raise KeyError(key)