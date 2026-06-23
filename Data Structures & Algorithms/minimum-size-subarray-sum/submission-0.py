from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        total = 0
        best = inf
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if best == inf else best


        