class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            for mx, my in moves:
                res += dfs(i + mx, j + my)
            return res

        return max(dfs(i, j) for i in range(n) for j in range(m))

        