class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        bought = float("-inf")
        
        for price in prices:
            bought, sold = max(bought, sold - price), max(sold, bought + price)

        return sold
        