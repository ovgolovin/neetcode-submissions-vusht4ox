class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_lower_bound(nums, target)


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


    def search_upper_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1


    def search_lower_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1
