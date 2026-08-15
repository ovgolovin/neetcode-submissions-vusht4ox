class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums, reverse=True)

        def dfs(i, curr_count, count, sum_, permutations, level):
            print(" " * level, i, curr_count, count, sum_, permutations)
            if sum_ == target:
                return permutations

            res = 0

            if sum_ + nums[i] <= target:
                res += dfs(
                    i,
                    curr_count + 1,
                    count + 1,
                    sum_ + nums[i],
                    permutations * (count + 1) // (curr_count + 1),
                    level + 1)    

            for j in range(i + 1, len(nums)):
                if sum_ + nums[j] <= target:
                    res += dfs(j, 1, count + 1, sum_ + nums[j], permutations * (count + 1), level + 1)

            return res

       
        return dfs(0, 0, 0, 0, 1, 0)