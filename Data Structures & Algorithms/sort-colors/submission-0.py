class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        p1 = 0
        p2 = len(nums)

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i < p2:
            if nums[i] == 0:
                swap(i, p1)
                p1 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                p2 -= 1
                swap(i, p2)


        