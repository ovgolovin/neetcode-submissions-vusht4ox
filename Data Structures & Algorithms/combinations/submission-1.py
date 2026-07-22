class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        comb = [0] * k

        def dfs(pos, start_val, k):
            for val in range(start_val, n - k + 2):
                comb[pos] = val
                if k == 1:
                    results.append(comb[:])
                else:
                    dfs(pos + 1, val + 1,  k - 1)



        dfs(0, 1, k)

        return results
        