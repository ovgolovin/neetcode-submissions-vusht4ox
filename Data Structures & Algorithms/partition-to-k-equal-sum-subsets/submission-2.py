from functools import cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        if max(nums) > target:
            return False

        @cache
        def dfs(candidates, used):
            if used % target == 0:
                if not candidates:
                    return True
                return dfs(candidates[1:], (used + candidates[0]) % target)

            for i, num in enumerate(candidates):
                if used + num > target:
                    continue

                if dfs(candidates[:i] + candidates[i+1:], (used + num) % target):
                    return True

            return False

        return dfs(
            tuple(sorted(nums, reverse=True)),
            0
        )

        