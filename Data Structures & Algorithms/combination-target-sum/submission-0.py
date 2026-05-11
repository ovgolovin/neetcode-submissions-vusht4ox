class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        def dfs(i, cur, total):
            if total == target:
                yield cur
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                yield from dfs(j, cur + [nums[j]], total + nums[j])
        
        return list(dfs(0, [], 0))
        