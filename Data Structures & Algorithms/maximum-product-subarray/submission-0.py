class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        pref = suf = 0
        for i in range(len(nums)):
            suf = nums[i] * (1 if suf == 0 else suf)
            pref = nums[n - 1 - i] * (1 if pref == 0 else pref)
            res = max(res, pref, suf)
        return res     