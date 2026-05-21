class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(rng):
            prev = curr = 0
            for i in rng:
                prev, curr = curr, max(prev + nums[i], curr)
            return curr

        return max(nums[0], helper(range(0, len(nums) - 1)), helper(range(1, len(nums))))
        