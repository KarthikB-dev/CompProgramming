from typing import List


class Solution:
    def mdigit(self, num):
      _max = -1
      for digit in str(num):
        if int(digit) > _max:
          _max = int(digit)
      return _max
    def maxSum(self, nums: List[int]) -> int:
      pairs = {}

      for i1, n1 in enumerate(nums):
        for i2, n2 in enumerate(nums):
          # check if the max digits are
          # equivalent, and if they are, add to
          # pairs
          if i1 != i2 and self.mdigit(n1) == self.mdigit(n2):
            pairs[(n1, n2)] = n1 + n2

      msum = -1
      if len(pairs) > 0:
        for pair, _sum in pairs.items():
          if _sum > msum:
            msum = _sum
            print(f"Pair: {pair[0]}, {pair[1]}")
      return msum

        