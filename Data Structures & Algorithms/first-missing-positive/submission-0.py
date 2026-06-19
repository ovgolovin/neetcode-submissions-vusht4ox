class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            nums[i] = max(0, num)

        for i in range(len(nums)):
            num = abs(nums[i])
            if num < 1 or num > len(nums):
                continue
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            elif nums[num - 1] == 0:
                nums[num - 1] = -(len(nums) + 1)

        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1

        return len(nums) + 1
        