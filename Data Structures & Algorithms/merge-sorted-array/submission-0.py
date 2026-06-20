class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(1, m + 1):
            nums1[len(nums1) - i] = nums1[m - i]

        i = j = 0
        while i < m and j < n:
            if nums1[len(nums1) - m + i] < nums2[j]:
                nums1[i + j] = nums1[len(nums1) - m + i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

        while i < m:
            nums1[i + j] = nums1[len(nums1) - m + i]
            i += 1

        while j < n:
            nums1[i + j] = nums2[j]
            j += 1

                
        