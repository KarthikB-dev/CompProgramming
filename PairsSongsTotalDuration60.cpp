#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        // Better algo: store hash map
        // key: time[i] % 60
        // value: frequency/counts that have that remainder
        long num = 0;
        unordered_map<long, long> mod_map;
        for (long song : time) {
            if (mod_map.count(song % 60) == 0) {
                mod_map[song % 60] = 1;
            }
            else {
                mod_map[song % 60] += 1;
            }
        }
        // pairs that can work: val1 + val2 = 60 or val1 = 0 or val2 = 0
        // constant time execution
        long double_count = 0;
        for (long i = 0; i < 60; i++) {
            for (long j = 0; j < 60; j++) {
                // If both values exist
                if (mod_map.count(i) && mod_map.count(j)) {
                    if (i == 0 && j == 0) {
                       // Should simply be the number of pairs 
                       num += (mod_map[0] * (mod_map[0] - 1)) / 2;
                    }
                    else if (i == 30 && j == 30) {
                       // Should simply be the number of pairs 
                       num += (mod_map[30] * (mod_map[30] - 1)) / 2;
                    }
                    else if (i + j == 60){
                        // Should be the number of pairs
                        double_count += mod_map[i] * mod_map[j];
                    }
                }
            }
        } 
        return num + double_count / 2;
    }
};

/*
Brute force algo:
 long num = 0;
 for (long i1 = 0; i1 < time.size() - 1; i1++) {
     for (long i2 = i1 + 1; i2 < time.size(); i2++) {
         if ((time[i1] + time[i2]) % 60 == 0) {
             num++;
         }
     }
 } 
 return num;
*/