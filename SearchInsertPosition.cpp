#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      int idx = 0;
      for (auto elem : nums) {
        if (elem >= target) {
          return idx;
        }
        idx += 1;
      } 
      return nums.size();
    }
};