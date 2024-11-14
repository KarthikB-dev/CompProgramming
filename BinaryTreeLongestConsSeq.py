from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, glob_max):
      curr_path = 1
      if not root:
        return 0

      lcall = self.dfs(root.left, glob_max)
      rcall = self.dfs(root.right, glob_max)

      glob_max[0] = max(glob_max[0], lcall)
      glob_max[0] = max(glob_max[0], rcall)

      add_l, add_r = curr_path, curr_path
      if root.left and root.left.val == root.val + 1:
        add_l += lcall
      if root.right and root.right.val == root.val + 1:
        add_r += rcall

      curr_path = max(add_l, add_r)
      glob_max[0] = max(glob_max[0], curr_path)

      return curr_path

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
      glob_max = [1]
      self.dfs(root, glob_max)
      return glob_max[0]