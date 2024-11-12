from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_iter = True
        curr_node = ListNode(0, None)
        head = None

        while list1 or list2:

            if list1 and list2:
                if list1.val < list2.val:
                    curr_node.next = ListNode(list1.val, None)
                    list1 = list1.next
                else:
                    curr_node.next = ListNode(list2.val, None)
                    list2 = list2.next
                curr_node = curr_node.next

            elif list1:
                curr_node.next = ListNode(list1.val, None)
                list1 = list1.next
                curr_node = curr_node.next
                
            elif list2:
                curr_node.next = ListNode(list2.val, None)
                list2 = list2.next
                curr_node = curr_node.next

            if first_iter:
                head = curr_node
                first_iter = False

        return head