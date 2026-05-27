class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.comb(m, n)

    def dp(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]


    def comb(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m

        res = 1
        for j in range(1, n):
            res *= (m + j - 1)
            res //= j
        return res
        