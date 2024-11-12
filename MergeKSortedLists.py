from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remaining(self, lists):
        for node in lists:
            if node:
                return True
        return False

    def min_idx(self, lists):
        min_val = float('inf')
        midx = -1
        for idx, node in enumerate(lists):
            if node and node.val < min_val:
                min_val = node.val
                midx = idx
        return midx
                

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        first_iter = True
        curr_node = ListNode(0, None) # Dummy node, will be deleted
        head = None

        while self.remaining(lists):
            midx = self.min_idx(lists)
            curr_node.next = ListNode(lists[midx].val, None)
            lists[midx] = lists[midx].next
            curr_node = curr_node.next

            if first_iter:
                head = curr_node
                first_iter = False

        return head