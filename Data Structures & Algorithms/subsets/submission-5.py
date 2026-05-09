class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:     
        def dfs(i, arr):
            if i == len(nums):
                yield arr
                return
            yield from dfs(i + 1, arr)
            yield from dfs(i + 1, arr + [nums[i]])
        
        return list(dfs(0, []))