# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

from bisect import bisect_left

class Solution:
    def guessNumber(self, n: int) -> int:
        search_space = range(1, n + 1)
        idx = bisect_left(
            search_space,
            True,
            key = lambda i: guess(i) < 1
        )
        return search_space[idx]
        