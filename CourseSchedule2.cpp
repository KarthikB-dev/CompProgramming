#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
      vector<int> L;
      vector<int> source;
      // Maps a course to its prereqs
      vector<set<int>> incoming(numCourses);
      vector<set<int>> outgoing(numCourses);

      for (int c = 0; c < numCourses; c++) {
        incoming[c] = {}; 
        outgoing[c] = {};
      }
      for (vector<int> pair : prerequisites) {
        int prereq = pair[1];
        int course = pair[0];
        incoming[course].insert(prereq);
        outgoing[prereq].insert(course);
      }

      // Constructing source
      for (int c = 0; c < numCourses; c++) {
        if (incoming[c].size() == 0) {
          source.push_back(c);
        }
      }
      
      while (source.size() > 0) {
        int n = source.back();
        source.pop_back();
        L.push_back(n); 
        for (int m : outgoing[n]) {
          // Remove the edge from n to e
          outgoing[n].erase(m);
          incoming[m].erase(n);
          // If m has no other incoming edges, insert m into S
          if (incoming[m].size() == 0) {
            source.push_back(m);
          }
        }
      }
      // If the graph has edges, return an empty array
      for (int c = 0; c < numCourses; c++) {
        if (outgoing[c].size() > 0) {
          return {};
        }
        else if (incoming[c].size() > 0) {
          return {};
        }
      }
      return L;
    }
};