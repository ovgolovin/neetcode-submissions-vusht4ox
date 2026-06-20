class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        last = None
        last_idx = -1
        for i in range(len(nums)):
            if nums[i] == last:
                continue
            last = nums[i]
            last_idx += 1
            nums[last_idx] = last
            k += 1
        return k
        