class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [0] * n
        for i in range(0, m):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j] += dp[j - 1] if j > 0 else 1
        return dp[n - 1]
                
        