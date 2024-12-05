class Solution:
    def smallestNumber(self, n: int) -> int:
      num = 1
      add = 2

      while num < n:
        num += add
        add *= 2

      return num