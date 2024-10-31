# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_length(self, head):
        curr_node = head
        length = 0
        while curr_node != None:
            curr_node = curr_node.next
            length += 1
        return length 

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: # type: ignore
        curr_node = head
        curr_idx = 0

        # O(n) time
        length = self.get_length(head)

        # O(n^2 time)
        mod_head = False
        while curr_idx + k <= length:
            # Reverse from [curr_idx, curr_idx + k)
            node_list = []

            iter_idx = curr_idx
            while iter_idx < curr_idx + k:
                node_list.append(curr_node)
                new_head = curr_node
                curr_node = curr_node.next
                iter_idx += 1
            
            # The first node in the next group of nodes
            # to be reversed
            next_group = curr_node

            if not mod_head:
                head = new_head
                mod_head = True

            node_list.reverse()

            for idx in range(len(node_list) - 1):
                node_list[idx].next = node_list[idx + 1]

            node_list[-1].next = next_group 
            # If linked_list[next_group + k] is not null, then
            # update node_list[-1].next to be that node
            if curr_idx + 2*k - 1 < length:
                jump_node = next_group
                # Iterate k - 1 times
                for __ in range(k - 1):
                    jump_node = jump_node.next
                node_list[-1].next = jump_node

            # Move to next group
            curr_node = next_group
            curr_idx = curr_idx + k

        # 0, 1, 2, 3, 4
        # 1, 2, 3, 4, 5

        return head