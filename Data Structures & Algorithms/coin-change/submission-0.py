class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        best_counts = [float("inf")] * (amount + 1)
        best_counts[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                best_counts[i] = min(best_counts[i], best_counts[i - coin] + 1)

        return best_counts[amount] if best_counts[amount] <= amount else -1