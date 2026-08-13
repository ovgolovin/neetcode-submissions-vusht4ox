class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False

        
        dp = [False] * n
        dp[0] = True
        farthest = 0

        for i in range(n):
            if not dp[i]:
                continue

            for farthest in range(max(farthest, i + minJump), min(i + maxJump + 1, n)):
                if s[farthest] == '0':
                    dp[farthest] = True
        
        return dp[n - 1]
        