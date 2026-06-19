class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            if len(window) == k:
                window.remove(nums[i - k])
            window.add(num)
        return False
        