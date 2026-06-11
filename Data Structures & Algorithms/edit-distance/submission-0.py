class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        m = len(word1)
        n = len(word2)

        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            dp_1_1 = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j], dp_1_1 = dp_1_1, dp[j]
                else:
                    dp[j], dp_1_1 = 1 + min(dp_1_1, dp[j], dp[j - 1]), dp[j]
        return dp[-1]


        