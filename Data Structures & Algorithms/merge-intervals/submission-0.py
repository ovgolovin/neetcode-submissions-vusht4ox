from itertools import islice

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for i, j in islice(intervals, 1, None):
            if i > res[-1][1]:
                res.append([i, j])
            else:
                res[-1][1] = max(res[-1][1], j)
        return res

        