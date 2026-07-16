from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        if max(matchsticks) > target:
            return False

        matchsticks.sort(reverse=True)
        n = len(matchsticks)

        # dp[mask] = partial length of the side currently being filled.
        #
        # -1: this subset cannot be built without overflowing some side
        #  0..target-1: valid subset; this is the current partial side sum
        dp = [-1] * (1 << n)

        # Empty subset: no sticks used, current side has length 0.
        dp[0] = 0

        # Process subsets from smaller masks toward full_mask.
        for mask in range(1 << n):
            current = dp[mask]

            # Skip subsets that cannot be arranged legally.
            if current == -1:
                continue

            # Try to add every stick not already included in mask.
            for i in range(n):
                if mask & (1 << i):
                    continue  # Stick i is already used.

                stick = matchsticks[i]

                # It may not overflow the side currently being filled.
                if current + stick > target:
                    continue

                next_mask = mask | (1 << i)

                # If current + stick == target:
                #   modulo gives 0, so this side is finished.
                #
                # Otherwise:
                #   it remains a partially filled current side.
                dp[next_mask] = (current + stick) % target

        full_mask = (1 << n) - 1

        # All sticks must be used and the final side must also close.
        return dp[full_mask] == 0