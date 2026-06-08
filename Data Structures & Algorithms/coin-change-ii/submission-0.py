class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(0, amount + 1 - coin):
                dp[a + coin] += dp[a]
        return dp[amount]