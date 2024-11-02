from queue import Queue
import math
from queue import Queue
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if not root:
            return 0

        left_max = max(self.dfs(root.left), 0) 
        right_max = max(self.dfs(root.right), 0)

        current_path_sum = root.val + left_max + right_max

        self.max_sum = max(self.max_sum, current_path_sum)

        return root.val + max(left_max, right_max)

    def maxPathSum(self, root) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum



def main():
    r2 = TreeNode(7, None, None)
    l2 = TreeNode(15, None, None)
    r1 = TreeNode(20, l2, r2)
    l1 = TreeNode(9, None, None)
    rt = TreeNode(-10, l1, r1)

    sol = Solution()
    mps = Solution.maxPathSum(sol, rt)
    print(f"Max Path Sum: {mps}")

if __name__ == "__main__":
    main()
