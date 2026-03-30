class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(0, len(nums) - 1):
            left[i + 1] = left[i] * nums[i]

        right = [1] * len(nums)
        for i in range(len(nums)-1, 0, -1):
            right[i - 1] = right[i] * nums[i]

        return [left[i] * right[i] for i in range(0, len(nums))]