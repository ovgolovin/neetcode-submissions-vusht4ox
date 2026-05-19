class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        if n == 0:
            return
        m = len(grid[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1 ,0)]

        def explore(i, j):
            stack = [(i, j, 0)]
            while stack:
                i, j, dist = stack.pop()
                if dist == -1 or dist != 0 and dist >= grid[i][j]:
                    continue
                grid[i][j] = dist
                for dx, dy in moves:
                    i_new = i + dx
                    if i_new < 0 or i_new >= n:
                        continue
                    j_new = j + dy
                    if j_new < 0 or j_new >= m:
                        continue
                    stack.append((i_new, j_new, dist + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    explore(i, j)



        