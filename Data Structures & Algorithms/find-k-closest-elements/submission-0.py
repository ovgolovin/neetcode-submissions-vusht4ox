from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        search_space = range(len(arr))
        start = bisect_left(
            search_space,
            0,
            lo = 0,
            hi = len(arr) - k,
            key = lambda i: arr[i + k] + arr[i] - 2 * x )

        return arr[start:start + k]

        