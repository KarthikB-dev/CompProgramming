from typing import List

def ending(iv):
    return iv[1]

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ivals = intervals
        ivals.sort(key=ending)
        num_int = len(intervals)
        for i in range(num_int - 1):
          if ivals[i][1] > ivals[i+1][0]:
              return False
        return True