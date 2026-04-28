class Solution:
    def findDuplicate(self, nums: List[int]) -> int:     
        res = 0
        for i in range(15):
            mask = 1 << i
            actual = sum(1 if (num & mask) else 0 for num in nums)
            expected = sum(1 if (num & mask) else 0 for num in range(1, len(nums)))
            if actual > expected:
                res |= mask
        return res