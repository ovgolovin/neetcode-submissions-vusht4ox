class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_sell = 0
        buy = float("-inf")
        sell = 0

        for price in prices:
            prev_buy = buy
            buy = max(prev_buy, prev_sell - price)
            prev_sell = sell
            sell = max(prev_sell, prev_buy + price)

        return sell        
        