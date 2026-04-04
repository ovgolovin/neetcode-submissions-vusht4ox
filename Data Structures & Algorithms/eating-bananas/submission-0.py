class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate_left = 1
        rate_right = max(piles) + 1
        while rate_left < rate_right:
            rate = rate_left + (rate_right - rate_left) // 2
            time = 0
            for pile in piles:
                time += (pile - 1) // rate + 1
            if time <= h:
                rate_right = rate
            else:
                rate_left = rate + 1
        return rate_left