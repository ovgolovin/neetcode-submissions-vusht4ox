class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def pivot(nums, l, r):
            med = l + (r - l) // 2
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] > nums[med]:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[med] < nums[r]:
                nums[med], nums[r] = nums[r], nums[med]

            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i


        def sort(nums, l, r):
            if r <= l:
                return
            if r == l + 1:
                if nums[l] > nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                return
                
            p = pivot(nums, l, r)
            sort(nums, l, p - 1)
            sort(nums, p + 1, r)

        sort(nums, 0, len(nums) - 1)

        return nums
