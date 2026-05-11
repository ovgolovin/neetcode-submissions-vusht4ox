class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = nums[:]
        def dfs(i):
            if i == len(nums):
                yield nums[:]
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                yield from dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        
        return list(dfs(0))
