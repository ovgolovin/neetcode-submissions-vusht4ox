class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = 0
        for num in nums:
            cur = max(0, cur)
            cur += num
            best = max(best, cur)
        return best
        