# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr_node = head
        nodes = []
        while curr_node:
            nodes.append(curr_node)
            curr_node = curr_node.next
        nodes[left - 1:right] = nodes[left - 1:right][::-1]
        
        for node_idx in range(len(nodes) - 1):
            nodes[node_idx].next = nodes[node_idx + 1]
        nodes[-1].next = None
        return nodes[0]