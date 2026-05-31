from bisect import bisect_left, bisect_right
from itertools import chain, islice

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, b = newInterval
        i = bisect_left(intervals, a, key = lambda x:x[0])
        if i > 0 and intervals[i-1][1] >= a:
            a = intervals[i-1][0]
            i -= 1

        j = bisect_right(intervals, b, lo=i, key = lambda x:x[0])
        if j > i and intervals[j-1][1] >= b:
            b = intervals[j-1][1]

        return list(chain(
            islice(intervals, 0, i),
            [[a, b]],
            islice(intervals, j, None)
        ))

        



        

