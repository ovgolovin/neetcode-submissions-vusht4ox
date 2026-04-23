import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


    def bisect_left(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l
















































    def search_iterative(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1


    def search_lower_bound(self, nums: List[int], target: int) -> int:
        # first index where a value is greater than or equal to the target
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1


    def search_upper_bound(self, nums: List[int], target: int) -> int:
        # first index where a value greater than the target appears
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1
