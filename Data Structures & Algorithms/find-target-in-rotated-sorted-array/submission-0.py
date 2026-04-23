class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        def binsearch(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    return binsearch(l, mid - 1)
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    return binsearch(mid + 1, r)
                else:
                    r = mid - 1

        return -1

