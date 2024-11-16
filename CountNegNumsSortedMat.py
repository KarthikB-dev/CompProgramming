from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
      num_neg = 0
      for row in grid:
        for idx, elem in enumerate(row):
          if elem < 0:
            num_neg += 1
            if idx < len(row) - 1:
              num_neg += (len(row) - 1 - idx)
              break
      return num_neg