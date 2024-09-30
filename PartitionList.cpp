/**
 * Definition for singly-linked list.
 * 
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* less_head = nullptr;
        ListNode* less_tail = nullptr;
        ListNode* greater_head = nullptr;
        ListNode* greater_tail = nullptr;

        // 1 4 3 2 5 2
        // x = 3
        // all nodes less than x come before nodes greater than or equal to x
        // order must be preserved in each of two partitions, but the overall order need not be preserved
        
        ListNode* curr_node = head;

        while (curr_node) {
            ListNode* insert_node = new ListNode(curr_node -> val, nullptr);
            if (curr_node -> val < x) {
                if (less_tail) {
                    less_tail -> next = insert_node;
                }
                less_tail = insert_node;

                if (less_head == nullptr) {
                    less_head = insert_node;
                }
            }
            else if (curr_node -> val >= x) {
                if (greater_tail) {
                    greater_tail -> next = insert_node;
                }
                greater_tail = insert_node;

                if (greater_head == nullptr) {
                    greater_head = insert_node;
                }
            }
            curr_node = curr_node -> next;
        }

        if (less_tail) {
            less_tail -> next = greater_head;
        }  
        return less_head ? less_head : greater_head;
    }
};