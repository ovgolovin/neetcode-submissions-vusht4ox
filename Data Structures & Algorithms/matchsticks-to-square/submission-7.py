from functools import lru_cache
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        if max(matchsticks) > target:
            return False

        sticks = tuple(sorted(matchsticks, reverse=True))

        @lru_cache(None)
        def dfs(
            deferred: tuple[int, ...],
            available: tuple[int, ...],
            current_sum: int,
        ) -> bool:
            if not available:
                return False

            stick = available[0]
            rest = available[1:]

            if current_sum + stick <= target:
                next_sum = (current_sum + stick) % target

                if next_sum == 0:
                    next_available = deferred + rest

                    if not next_available:
                        return True

                    if dfs((), next_available, 0):
                        return True

                elif dfs(deferred, rest, next_sum):
                    return True

            # Optional symmetry pruning: at the beginning of a side,
            # require the largest remaining stick to be used.
            if current_sum == 0:
                return False

            return dfs(deferred + (stick,), rest, current_sum)

        return dfs((), sticks, 0)