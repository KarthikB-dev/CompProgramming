from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.nums = nums
       self.nums.sort()
       self.k = k 

    def add(self, val: int) -> int:
        inserted = False
        for idx, ele in enumerate(self.nums):
            if ele > val:
                self.nums.insert(idx, val)
                inserted = True
                break
        if not inserted:
            self.nums.append(val)
        return self.nums[-1 * self.k]