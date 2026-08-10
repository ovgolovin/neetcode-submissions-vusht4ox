class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        p1 = 0
        p2 = len(nums)

        while i < p2:
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                i += 1
                p1 += 1
            elif nums[i] == 1:
                i += 1
            else: # 2
                p2 -= 1
                nums[i], nums[p2] = nums[p2], nums[i]


        