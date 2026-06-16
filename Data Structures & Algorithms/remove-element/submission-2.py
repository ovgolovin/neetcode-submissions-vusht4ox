class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val > 50:
            return len(nums)
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                k -= 1
                nums[i] = nums[k]
            else:
                i += 1
        return k
        