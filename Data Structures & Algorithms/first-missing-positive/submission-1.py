class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] < 1 or nums[i] > n:
                i += 1
                continue

            target = nums[i] - 1
            if nums[target] == nums[i]:
                i += 1
            else:
                nums[i], nums[target] = nums[target], nums[i]

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        
        return n + 1
        
        