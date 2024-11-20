#include <bits/stdc++.h>
#include<unordered_set>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void add_vals(TreeNode* root1, unordered_set<int>& t1) {
      if (root1) {
        t1.insert(root1->val);
        add_vals(root1 -> left, t1);
        add_vals(root1 -> right, t1);
      }
    }
    bool check_sum(TreeNode* root2, unordered_set<int>& t1, int target) {
      if (root2) {
        if (t1.contains(target - root2->val)) {
          return true;
        }
        bool lcall = check_sum(root2 -> left, t1, target);
        bool rcall = check_sum(root2 -> right, t1, target);
        return lcall || rcall;
      }
      return false;
    }
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
       unordered_set<int> t1; 
       add_vals(root1, t1);
       return check_sum(root2, t1, target);
    }
};