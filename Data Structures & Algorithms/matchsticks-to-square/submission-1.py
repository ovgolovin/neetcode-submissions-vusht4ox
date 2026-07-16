from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        if max(matchsticks) > target:
            return False

        # Larger sticks first: improves pruning, not correctness.
        matchsticks.sort(reverse=True)

        def dfs(remaining: tuple[int, ...], current_sum: int) -> bool:
            """
            remaining:
                Sticks that have not been placed yet.

            current_sum:
                Length already built on the currently open side.

                current_sum == 0 means:
                - no side is currently in progress, or
                - we just completed a side and are starting the next.
            """

            # No sticks left: valid only if the last side ended exactly.
            if not remaining:
                return current_sum == 0

            # Try every remaining stick as the next stick in the
            # sequential side-building stream.
            previous = None

            for i, stick in enumerate(remaining):
                # Equal sticks create equivalent branches at this level.
                if stick == previous:
                    continue
                previous = stick

                # This stick cannot fit on the currently open side.
                if current_sum + stick > target:
                    continue

                # Remove this one stick from the remaining collection.
                next_remaining = remaining[:i] + remaining[i + 1:]

                # If sum reaches target, modulo resets it to 0:
                # close this side and start the next side.
                next_sum = (current_sum + stick) % target

                if dfs(next_remaining, next_sum):
                    return True

                # If this was an empty side and the largest currently
                # available stick did not lead to a solution, trying
                # another stick as the first stick of that same side is
                # still necessary in general, so do not return here.

            return False

        return dfs(tuple(matchsticks), 0)