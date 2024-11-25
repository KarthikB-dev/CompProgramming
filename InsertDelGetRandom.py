import random

class RandomizedSet:

    def __init__(self):
        self.nums_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.nums_dict:
            return False
        else:
            self.nums_dict[val] = True
            return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_dict:
            return False
        del self.nums_dict[val]
        return True

    def getRandom(self) -> int:
        key, __ =  random.choice(list(self.nums_dict.items()))
        return key
