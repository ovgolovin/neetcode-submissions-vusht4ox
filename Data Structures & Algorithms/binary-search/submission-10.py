import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.bisect_right(nums, target)
        return index - 1 if index > 0 and nums[index - 1] == target else -1


    def bisect_right(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l



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
