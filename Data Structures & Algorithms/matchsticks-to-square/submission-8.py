from functools import cache

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)

        if not matchsticks or matchsticks[0] > target:
            return False

        n = len(matchsticks)

        @cache
        def dfs(mask: int) -> bool:
            used_sum = sum(
                matchsticks[i]
                for i in range(n)
                if mask & (1 << i)
            )
            current_sum = used_sum % target

            if mask == (1 << n) - 1:
                return current_sum == 0

            for i, stick in enumerate(matchsticks):
                if not (mask & (1 << i)) and current_sum + stick <= target:
                    if dfs(mask | (1 << i)):
                        return True

            return False

        return dfs(0)