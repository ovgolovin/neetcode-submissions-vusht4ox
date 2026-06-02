from itertools import islice

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[1])
        res = 0
        last_end = intervals[0][1]
        for start, end in islice(intervals, 1, None):
            if last_end > start:
                res += 1
            else:
                last_end = end
        return res

        