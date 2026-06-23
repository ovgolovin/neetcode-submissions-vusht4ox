import bisect

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            rem = cap
            day = 1
            for w in weights:
                if w > rem:
                    if day == days:
                        return False
                    day += 1
                    rem = cap
                rem -= w
            return True

        search_space = range(max(weights), sum(weights) + 1)

        idx = bisect.bisect_left(
            search_space,
            True,
            key = lambda cap: can_ship(cap)
        )

        return search_space[idx]


        