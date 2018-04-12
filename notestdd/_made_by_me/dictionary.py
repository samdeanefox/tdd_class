"""Create a working dictionary from scratch"""

class Dict:
    "Custom dictionary re-implementation of Python's built-n dict."

    def __init__(self):
        self.my_keys = []
        self.my_values = []

    def __getitem__(self, key):
        try:
            position = self.my_keys.index(key)
            return self.my_values[position]
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        self.my_keys.append(key)
        self.my_values.append(value)

        print('hi')