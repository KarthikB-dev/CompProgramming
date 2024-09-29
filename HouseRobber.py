class Solution:
    def rob(self, nums: List[int]) -> int:
        # The max money you can earn considering the first i houses is
        # is dp[i - 2] + num[i], dp[i - 1]

        max_earn = {0: nums[0]}
        nums_len = len(nums)

        # Bases cases
        if nums_len == 1:
            return nums[0]

        elif nums_len == 2:
            return max(nums[0], nums[1])

        max_earn[1] = max(nums[0], nums[1])

        for idx in range(2, nums_len):
            max_earn[idx] = max(max_earn[idx - 2] + nums[idx], max_earn[idx - 1]) 

        return max_earn[nums_len - 1]