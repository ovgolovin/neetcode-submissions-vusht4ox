class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k

        if max(nums) > target:
            return False

        def dfs(next_bucket, this_bucket, bucket_sum):
            if bucket_sum % target == 0:
                if not next_bucket and not this_bucket:
                    return True
                candidates = next_bucket + this_bucket
                return dfs((), candidates[1:], (bucket_sum + candidates[0]) % target)

            for i in range(len(this_bucket)):
                if bucket_sum + this_bucket[i] > target:
                    continue
                
                if i > 0 and this_bucket[i-1] == this_bucket[i]:
                    continue

                if dfs(next_bucket + this_bucket[:i], this_bucket[i+1:], (bucket_sum + this_bucket[i]) % target):
                    return True

            return False

        return dfs(
            (),
            tuple(sorted(nums, reverse=True)),
            0
        )

        