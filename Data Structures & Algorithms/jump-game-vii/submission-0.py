class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False

        
        dp = [False] * n
        dp[0] = True
        fartherst = 0

        for i in range(n):
            if dp[i] == False:
                continue

            for fartherst in range(max(fartherst, i + minJump), min(i + maxJump + 1, n)):
                if s[fartherst] == '0':
                    dp[fartherst] = True
        
        return dp[n - 1]
        