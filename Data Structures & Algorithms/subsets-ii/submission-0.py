class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        def dfs(i, subset):
            yield subset

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                yield from dfs(j + 1, subset + [nums[j]])


        return list(dfs(0, []))

        