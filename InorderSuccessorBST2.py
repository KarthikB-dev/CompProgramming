# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def get_min(self, node):
      if not node:
        return None
      curr_node = node
      while curr_node.left:
        curr_node = curr_node.left
      return curr_node
      
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
      if not node:
        return None
      elif node.right:
        return self.get_min(node.right)
      else:
        curr_node = node.parent
        while curr_node:
          if curr_node.val > node.val:
            return curr_node
          curr_node = curr_node.parent
        return None