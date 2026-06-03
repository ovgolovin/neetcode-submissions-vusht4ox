class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, rem = divmod(sum(nums), 2)
        if rem != 0:
            return False
        
        dp = 1

        for num in nums:
            dp |= dp << num

        return dp & (1 << target) > 0

        