class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = float("+inf")
        res = 0
        for price in prices:
            res += max(0, price - prev)
            prev = price
        return res

        