from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lasts = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if lasts[-1] < num:
                lasts.append(num)
                continue
            
            lasts[bisect_left(lasts, num)] = num
        return len(lasts)

        