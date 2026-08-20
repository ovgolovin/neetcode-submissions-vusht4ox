class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(l, r):
            mid = l + (r - l) // 2
            if nums[l] > nums[r]:
                swap(l, r)
            if nums[l] > nums[mid]:
                swap(l, mid)
            elif nums[mid] > nums[r]:
                swap(mid, r)

            swap(l + 1, mid)
            pivot = nums[l + 1]
            i = l + 1
            j = r

            while True:
                while True:
                    i += 1
                    if nums[i] >= pivot:
                        break

                while True:
                    j -= 1
                    if nums[j] <= pivot:
                        break

                if i > j:
                    break

                swap(i, j)

            swap(l + 1, j)
            return j


        def qsort(l, r):
            if r < l + 1:
                return
            elif r == l + 1:
                if nums[l] > nums[r]:
                    swap(l, r)
                return

            pivot = partition(l, r)
            qsort(l, pivot - 1)
            qsort(pivot + 1, r)

        qsort(0, len(nums) - 1)

        return nums
        

            
