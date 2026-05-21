class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        cur = 0
        for num in nums:
            cur = max(0, cur)
            cur += num
            total = max(total, cur)
        return total
        