#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int longestSubarray(vector<int>& nums) {
            // The structure suggests dynamic programming
            // Longest subarray leading up to that point
            // Or rather, the longest subarray *including* the 
            // current number
    
            // Solution: change one of the numbers to 0 then compute
            // a) if there is already a 0, do nothing
            // b) if the vector is all 1s, simply return the length - 1 (done!)
    
            // Caveat: you must find the *optimal* number to delete
            // suppose there are n instances of 0. You must find all 
            // table entries preceding a 0, their subarray lengths, 
            // and find the deletion that maximizes the resutling subarray.
            // Note that this must involve deletion of subarrays separated by a 0.
            // Finally, compare this to the length of the largest subarray computed in
            // the original dp table
    
            int n = nums.size();
            vector<int> dp_table(n);
            vector<int> len_table;
            int max_sub = 0;
    
    
            bool found_zero = false;
            for (int i = 0; i < n; i++) {
                if (nums[i] == 0) {
                    found_zero = true;
                }
            }
            if (!found_zero) {
                return n - 1;
            }
    
    
            if (nums[0] == 1) {
                dp_table[0] = 1;
            }
            else {
                dp_table[0] = 0;
            }
    
    
            for (int i = 1; i < nums.size(); i++) {
                if (nums[i] == 1) {
                    dp_table[i] = 1 + dp_table[i - 1];
                    if (dp_table[i] > max_sub) {
                        max_sub = dp_table[i];
                    }
                }
                else {
                    dp_table[i] = 0;
                }
            }
    
            // Alternative: push 0 to the table if you haven't found 
            // a subarray of consecutive 1s, otherwise simply push back
            // the length of that subarray
            int curr_sub = 0;
            for (auto elem : dp_table) {
                if (elem == 0) {
                    if (curr_sub != 0) {
                        len_table.push_back(curr_sub);
                        curr_sub = 0;
                    }
                    len_table.push_back(0);
                }
                else {
                    curr_sub++;
                }
            }
    
            len_table.push_back(curr_sub);
    
            for (int i = 0; i < len_table.size(); i++) {
                cout << i << ": " << len_table[i] << endl;
            }
    
            for (int i = 0; i < len_table.size(); i++) {
                if (i >= 2) {
                    if ((len_table[i] + len_table[i - 2]) > max_sub) {
                       max_sub = len_table[i] + len_table[i - 2];
                    }
                }     
            }
    
            return max_sub;
        }
    };