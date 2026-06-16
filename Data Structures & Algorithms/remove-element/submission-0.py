class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[j] == val:
                k -= 1
                j -= 1
            elif nums[i] == val:
                k -= 1
                nums[i] = nums[j]
                i += 1
                j -= 1
            else:
                i += 1
        return k
        