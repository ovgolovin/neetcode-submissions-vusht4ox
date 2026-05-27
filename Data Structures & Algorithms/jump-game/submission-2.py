class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        best = 0
        for i in range(n):
            if i > best:
                return False
            best = max(best, i + nums[i])
            if best >= n-1:
                return True
        return False
        