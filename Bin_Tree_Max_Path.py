from queue import Queue
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def get_list(self, root) -> list:
        # Allow for 1 indexing
        res = [None]
        q = Queue()
        q.put(root)

        while not q.empty():
            curr_node = q.get()
            if curr_node:
                res.append(curr_node.val)
            else:
                res.append(curr_node)

            if curr_node:
                q.put(curr_node.left)
                q.put(curr_node.right)

        return res

    def maxPathSum(self, root) -> int:
        # Stores path distances a node and its descendant
        tree_list = self.get_list(root)
        # Lowest possible sum is 
        # 3 * 1e4 * -1000, so this value has some buffer
        max_sum = 4 * 1e4 * -1000
        print(f"Tree list: {tree_list}")

        tree_indices = []
        for idx, val in enumerate(tree_list):
            if val != None:
                tree_indices.append(idx)

        # DP table where the keys are tuples, and the value is
        # the path cost
        dp = {}

        for outer in range(len(tree_indices)):
            for inner in range(outer, len(tree_indices)):
                i = tree_indices[outer]
                j = tree_indices[inner]

                i_depth = int(math.log2(i)) + 1
                j_depth = int(math.log2(j)) + 1
                # Same node -> path cost of 0
                if i == j:
                    dp[(i, j)] = tree_list[i]
                # Share the same parent -> sum of their path costs
                # and their parent
                elif i / 2 == j / 2:
                    dp[(i, j)] = tree_list[i] + tree_list[j] + tree_list[i // 2]
                # Same depth, but not same parent -> move up
                # and add current costs
                elif i_depth == j_depth:
                    dp[(i, j)] = tree_list[i] + tree_list[j] + dp[(i // 2, j // 2)]
                # i has greater depth than j -> move i up, leave j where it is
                elif i_depth > j_depth:
                    dp[(i, j)] = tree_list[i] + dp[(i // 2, j)]
                # j has greater depth than i -> move j up, leave i where it is
                else:
                    dp[(i, j)] = tree_list[j] + dp[(i, j // 2)]

                if dp[(i, j)] > max_sum:
                    max_sum = dp[(i, j)]

        return max_sum

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
