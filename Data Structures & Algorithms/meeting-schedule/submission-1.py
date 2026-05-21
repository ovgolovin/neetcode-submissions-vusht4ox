"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from itertools import pairwise

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i1, i2 in pairwise(sorted(intervals, key=lambda x: x.start)):
            if i1.end > i2.start:
                return False
        return True
