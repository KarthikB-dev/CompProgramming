#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) {
            return "1";
        }        
        // process the recursive call
        // keep track of the previous characters and their counts
        stringstream output;
        string rec_call = countAndSay(n - 1);
        char prev_char = rec_call[0];
        int curr_count = 0;
        int idx = 0;
        for (char curr_char : rec_call) {
            // increment the number of matches if the current character
            // matches the previous
            if (curr_char == prev_char) {
                curr_count += 1;
            }
            // if it doesn't match, then output it and reset the counter
            if (curr_char != prev_char) {
                output << curr_count << prev_char; 
                curr_count = 1;
            }
            // if you've reached the end of the string, then output
            // what you have
            if (idx == rec_call.length() - 1) {
                output << curr_count << curr_char;
            }
            prev_char = curr_char;
            idx += 1;
        }
        return output.str();
    }
};