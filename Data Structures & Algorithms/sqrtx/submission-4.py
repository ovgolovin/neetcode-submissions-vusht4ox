class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        res = self.mySqrt(x >> 2) << 1
        return res if (res + 1) * (res + 1) > x else res + 1