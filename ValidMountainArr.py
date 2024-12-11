from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
      idx = 1
      inc = True

      while idx < len(arr) - 1:
        if arr[idx] > arr[idx - 1]:
          idx += 1
          inc = False
        else:
          idx += 1
          break

      if not inc:
        while idx < len(arr):
          if arr[idx] >= arr[idx - 1]:
            return False
          idx += 1
        return True
      else:
        return False