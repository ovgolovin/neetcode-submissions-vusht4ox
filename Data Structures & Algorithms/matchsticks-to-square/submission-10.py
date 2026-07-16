from functools import cache

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        side = total // 4

        if max(matchsticks) > side:
            return False

        n = len(matchsticks)

        matchsticks = sorted(matchsticks, reverse=True)

        @cache
        def dfs(mask):
            cur_sum = sum(
                size
                for i, size in enumerate(matchsticks)
                if mask & (1 << i)
            ) % side

            if mask == (1 << n) - 1:
                return cur_sum == 0

            
            for i, size in enumerate(matchsticks):
                if mask & (1 << i):
                    continue
                if cur_sum + size > side:
                    continue
                if dfs(mask | (1 << i)):
                    return True
            
            return False


        return dfs(0)



