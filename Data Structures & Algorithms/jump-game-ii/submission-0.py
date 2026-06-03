class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        r = l = 0
        while r < len(nums) - 1:
            res += 1
            best = 0
            for i in range(l, r + 1):
                best = max(best, nums[i] + i)
                if best > len(nums) - 2:
                    break
            l = r + 1
            r = best
        return res 