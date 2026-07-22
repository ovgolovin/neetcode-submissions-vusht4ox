class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        comb = [0] * k

        def dfs(pos: int, start: int) -> None:
            if pos == k:
                results.append(comb[:])
                return

            for value in range(start, n - k + pos + 2):
                comb[pos] = value
                dfs(pos + 1, value + 1)

        dfs(0, 1)
        return results