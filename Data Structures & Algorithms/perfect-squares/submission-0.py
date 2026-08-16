class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for cand in range(1, n + 1):
                squared = cand * cand
                if squared > n:
                    break

                dp[target] = min(dp[target], 1 + dp[target - squared])

        return dp[n]    
            