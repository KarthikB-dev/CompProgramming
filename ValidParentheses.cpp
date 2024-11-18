#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
      stack<char> symb;
      unordered_map<char, char> close;
      close['('] = ')';
      close['{'] = '}';
      close['['] = ']';
      for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
          symb.push(c);
        }
        else {
          if (symb.size() && c == close[symb.top()]) {
            symb.pop();
          }
          else {
            cout << c << endl;
            return false;
          }
        }
      }
      return symb.size() == 0;
    }
};