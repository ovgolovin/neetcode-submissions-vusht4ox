class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, arr):
            if i == len(nums):
                res.append(arr)
                return
            dfs(i + 1, arr)
            dfs(i + 1, arr + [nums[i]])
        dfs(0, [])
        return res