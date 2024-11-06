from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1] - 2:
                return nums[idx] + 1
        return nums[-1] + 1