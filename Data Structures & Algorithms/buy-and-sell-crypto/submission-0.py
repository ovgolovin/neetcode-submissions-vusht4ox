class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        low = prices[0]
        best = 0
        for i in range(1, len(prices)):
            best = max(best, prices[i] - low)
            low = min(low, prices[i])
        return best