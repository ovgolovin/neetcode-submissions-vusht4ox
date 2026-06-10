class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        
        def cost(i):
            if i == -1 or i == n:
                return 1
            return nums[i]
        
        dp = [[0] * n for _ in range(n)]

        for r in range(0, n):
            for l in range(r, -1, -1):
                for i in range(l, r + 1):
                    price = cost(l - 1) * cost(i) * cost(r + 1)
                    price += dp[l][i - 1] if i > l else 0
                    price += dp[i + 1][r] if i < r else 0
                    dp[l][r] = max(dp[l][r], price) 
        return dp[0][n - 1]


        