class Solution:
    # K is k mod length - see below
    # 1, 2, 3, 4, 5
    # 5, 1, 2, 3, 4 (1)
    # 4, 5, 1, 2, 3 (2)
    # 3, 4, 5, 1, 2 (3)
    # 2, 3, 4, 5, 1 (4)
    # 1, 2, 3, 4, 5 (5), which is the same as doing nothing
    def rotate(self, nums: List[int], k: int) -> None: # type: ignore
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        k = k % length

        trailer = nums[length - k: ]
        header = nums[:length - k ]

        print(f"Trailer: {trailer}")
        print(f"Header: {header}")

        out = trailer + header
        for idx in range(len(nums)):
            nums[idx] = out[idx]