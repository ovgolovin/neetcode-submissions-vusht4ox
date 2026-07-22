class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        comb = [0] * k

        def dfs(index, start, remain):
            for val in range(start, n - remain + 2):
                comb[index] = val
                if remain == 1:
                    results.append(comb[:])
                else:
                    dfs(index + 1, val + 1,  remain - 1)



        dfs(0, 1, k)

        return results
        