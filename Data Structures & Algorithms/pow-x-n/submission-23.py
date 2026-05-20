class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        is_neg = n < 0
        n = abs(n)

        res = 1

        while n:
            n, remainder = divmod(n, 2)
            res *= 1 + (x - 1) * remainder
            x *= x

        return 1 / res if is_neg else res   