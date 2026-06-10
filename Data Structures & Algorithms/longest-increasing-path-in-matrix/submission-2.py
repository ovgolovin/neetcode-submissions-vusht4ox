class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[None] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            res = 1
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            dp[i][j] = res
            return res

        return max(dfs(i, j) for i in range(m) for j in range(n))
        