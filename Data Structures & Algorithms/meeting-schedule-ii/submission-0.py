"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from itertools import chain

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeline = sorted(chain.from_iterable((((interval.start, 1), (interval.end, -1)) for interval in intervals)))
        res = 0
        cum = 0
        for time, val in timeline:
            cum += val
            res = max(res, cum)
        return res