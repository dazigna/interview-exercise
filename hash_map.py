
from dataclasses import dataclass


@dataclass
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        

class CustomHashMap:
    def __init__(self, n) -> None:
        self.size = n
        self.table = [[] for _ in range(1, self.size)]

    def _hash(self, key):
        return key % self.size

    def get(self, key):
        hash_index = self._hash(key)
        for item in self.table[hash_index]:
            if item == key:
                return item
        raise KeyError('key not found')

    def set(self, key, value):
        hash_index = self._hash(key)
        for item in self.table[hash_index]:
            if item == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def remove(self, key):
        hash_index = self._hash(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('key not found')



