class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = 0

        for num in nums:
            cur += num
            best = max(best, cur)
            cur = max(cur, 0)

        return best
        