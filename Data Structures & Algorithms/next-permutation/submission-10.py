import bisect

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = bisect.bisect_left(range(n), 0, lo=i+1, hi=n, key=lambda x: nums[i] - nums[x]) - 1
            print(i, j)
            nums[i], nums[j] = nums[j], nums[i]

        l = i + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1   
        