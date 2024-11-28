class MapSum:

    def __init__(self):
        self.ms = {}

    def insert(self, key: str, val: int) -> None:
        self.ms[key] = val

    def sum(self, prefix: str) -> int:
        s = 0
        for k in self.ms:
          if len(prefix) <= len(k):
            if k[0:len(prefix)] == prefix:
              s += self.ms[k]
        return s