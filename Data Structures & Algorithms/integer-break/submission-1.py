class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        rem = n % 3
        if rem == 0:
            return 3 ** (n // 3)
        elif rem == 1:
            return 3 ** (n // 3 - 1) * 4
        else: # rem == 2
            return 3 ** (n // 3) * 2
