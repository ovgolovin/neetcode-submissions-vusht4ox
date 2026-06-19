class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = {
            0: 1
        }
        
        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            res += prefix_sum_counts.get(prefix_sum - k, 0)
            prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1

        return res
        