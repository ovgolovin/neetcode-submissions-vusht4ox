class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        