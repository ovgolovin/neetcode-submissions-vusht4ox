class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            prev_diag = dp[0]
            dp[0] = i == 0
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    prev_diag = dp[j]
                    dp[j] = dp[j - 1]
                    continue
                match = i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                prev_top = dp[j]
                if j < len(p) and p[j] == '*':
                    dp[j] = dp[j - 1] or (dp[j] and match)
                elif match:
                    dp[j] = prev_diag
                else:
                    dp[j] = False
                prev_diag = prev_top
        return dp[-1]
                

        