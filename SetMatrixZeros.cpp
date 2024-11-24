#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
       int m = matrix.size(); 
       int n = matrix[0].size();

       unordered_set<int> zrows;
       unordered_set<int> zcols;

       for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (matrix[r][c] == 0) {
                zrows.insert(r);
                zcols.insert(c);
            }
        }
       }

       for (int row : zrows) {
        for (int c = 0; c < n; c++) {
            matrix[row][c] = 0;
        }
       }
       for (int col : zcols) {
        for (int r = 0; r < m; r++) {
            matrix[r][col] = 0;
        }
       }
    }
};