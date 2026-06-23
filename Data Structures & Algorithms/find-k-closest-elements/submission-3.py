from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        search_space = range(len(arr) - k)
        
        # We want to find the first index 'i' where the element at 'i + k' 
        # is closer to 'x' than the element at 'i'.
        # Since True > False in Python, bisect_left searching for True 
        # will find the first index where this condition holds.
        start = bisect_left(
            search_space,
            True,
            key=lambda i: (x - arr[i]) <= (arr[i + k] - x)
        )

        return arr[start:start + k]

        