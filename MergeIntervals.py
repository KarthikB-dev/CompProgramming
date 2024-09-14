class Solution:
    def compare_end(start, end):
        return end 

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the end of the interval
        intervals.sort(key=self.compare_end)
        output = []
        num_intervals = len(intervals)
        for idx, interval in enumerate(intervals):
            # check for merging: current interval's start
            # is before or after the last one's end
            if idx > 0: 
                if interval[0] <= output[-1][1]:
                    # merging
                    if interval[1] > output[-1][1]:
                        output[-1][1] = interval[1]
                else:
                    output.append(interval)
            else:
                output.append(interval)
        return output