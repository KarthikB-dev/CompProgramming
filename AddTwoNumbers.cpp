/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* output = new ListNode;
        ListNode* lastNode = output;
        int carry = 0;
        while (l1 || l2) {
            if (l1) {
                lastNode -> val += l1->val;
            }
            if (l2) {
                lastNode -> val += l2->val;
            }
            lastNode -> val += carry; 
            carry = lastNode->val / 10;
            lastNode->val = lastNode->val % 10;

            // If either node has a node that follows it
            if (l1 && l1->next || l2 && l2->next) {
                ListNode* newNode = new ListNode();
                lastNode->next = newNode;
                lastNode = newNode;
            }
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        // Overflow
        if (carry > 0) {
            ListNode* newNode = new ListNode(carry);
            lastNode->next = newNode;
            lastNode = newNode;
        }
        return output;
    }
};