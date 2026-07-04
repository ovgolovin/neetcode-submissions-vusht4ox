class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best_min = best_max = nums[0]
        curr_min = curr_max = 0
        total = 0

        for num in nums:
            total += num

            curr_min = min(curr_min + num, num)
            curr_max = max(curr_max + num, num)

            best_min = min(best_min, curr_min)
            best_max = max(best_max, curr_max)

        
        return max(best_max, total - best_min) if best_max > 0 else best_max