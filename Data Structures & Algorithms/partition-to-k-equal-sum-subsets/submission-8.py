class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        if max(nums) > target:
            return False

        def dfs(defered, available, bucket_sum):
            if bucket_sum % target == 0:
                if not defered and not available:
                    return True
                candidates = defered + available
                return dfs((), candidates[1:], (bucket_sum + candidates[0]) % target)

            for i in range(len(available)):
                if bucket_sum + available[i] > target:
                    continue
                
                if i > 0 and available[i-1] == available[i]:
                    continue

                if dfs(defered + available[:i], available[i+1:], (bucket_sum + available[i]) % target):
                    return True

            return False

        return dfs(
            (),
            tuple(sorted(nums, reverse=True)),
            0
        )

        