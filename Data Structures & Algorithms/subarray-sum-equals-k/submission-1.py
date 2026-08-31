class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum_counts = {
            0: 1
        }

        res = 0
        pref_sum = 0

        for num in nums:
            pref_sum += num
            complement = pref_sum - k
            res += pref_sum_counts.get(complement, 0)
            pref_sum_counts[pref_sum] = pref_sum_counts.get(pref_sum, 0) + 1

        return res

        