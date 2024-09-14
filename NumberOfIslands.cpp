#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // marks all adjacent land locations 
    void explore(vector<vector<char>>& grid, vector<vector<bool>>& marked, int row, int col) {
        if (grid[row][col] == '1') {
            marked[row][col] = true;
            int m = grid.size();
            int n = grid[0].size();
            if (row > 0 && !marked[row - 1][col]) {
                explore(grid, marked, row - 1, col);
            }
            if (row < m - 1 && !marked[row + 1][col]) {
                explore(grid, marked, row + 1, col);
            }
            if (col > 0 && !marked[row][col - 1]) {
                explore(grid, marked, row, col - 1);
            }
            if (col < n - 1 && !marked[row][col + 1]) {
                explore(grid, marked, row, col + 1);
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int num_islands = 0;        
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> marked(m, vector<bool>(n, false));
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (!marked[row][col] && grid[row][col] == '1') {
                    explore(grid, marked, row, col);
                    num_islands += 1;
                }
            }
        }
        return num_islands;
    }
};