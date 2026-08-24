class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate_lo = 1
        rate_hi = max(piles) + 1

        while rate_lo < rate_hi:
            rate = rate_lo + (rate_hi - rate_lo) // 2
            time = sum((pile - 1) // rate + 1 for pile in piles)
            if time <= h:
                rate_hi = rate
            else:
                rate_lo = rate + 1
        
        return rate_lo