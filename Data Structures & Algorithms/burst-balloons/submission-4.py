class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded = [1] + nums + [1]
        n = len(padded)
        dp = [[0] * n for _ in range(n)]

        for r in range(0, n):
            for l in range(r, -1, -1):
                for i in range(l + 1, r):
                    price = padded[l] * padded[i] * padded[r]
                    price += dp[l][i] + dp[i][r]
                    dp[l][r] = max(dp[l][r], price)
                    
        return dp[0][n - 1]