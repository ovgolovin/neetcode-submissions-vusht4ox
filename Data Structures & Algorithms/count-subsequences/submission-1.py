class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [0] * n
        for i in range(0, m):
            prev = 1
            for j in range(0, n):
                curr = dp[j]
                if s[i] == t[j]:
                    curr += prev
                prev = dp[j]
                dp[j] = curr
        return dp[n - 1]
                
        