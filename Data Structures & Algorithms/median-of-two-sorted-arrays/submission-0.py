class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        t_mid = (len(nums1) + len(nums2)) // 2


        a_l = 0
        a_r = len(nums1)
        while True:
            a_mid = (a_l + a_r) // 2
            b_mid = t_mid - a_mid
            
            if ((a_mid == 0 or b_mid == len(nums2) or nums1[a_mid - 1] <= nums2[b_mid]) and
                (b_mid == 0 or a_mid == len(nums1) or nums2[b_mid - 1] <= nums1[a_mid])):
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return nums1[a_mid] if b_mid == len(nums2) else nums2[b_mid] if a_mid == len(nums1) else min(nums1[a_mid], nums2[b_mid])
                else:
                    return ((nums1[a_mid] if b_mid == len(nums2) else nums2[b_mid] if a_mid == len(nums1) else min(nums1[a_mid], nums2[b_mid]))
                        + (nums1[a_mid - 1] if b_mid == 0 else nums2[b_mid - 1] if a_mid == 0 else max(nums1[a_mid - 1], nums2[b_mid - 1]))
                        ) / 2.0

            elif a_mid > 0 and nums1[a_mid - 1] > nums2[b_mid]:
                a_r = a_mid - 1
            else:
                a_l = a_mid + 1
                