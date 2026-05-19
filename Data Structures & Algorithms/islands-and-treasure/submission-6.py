class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        if n == 0:
            return
        m = len(grid[0])
        inf = 2147483647

        moves = [(0, 1), (0, -1), (1, 0), (-1 ,0)]


        front = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]

        dist = 0
        while front:
            new_front = []
            for i, j in front:
                for dx, dy in moves:
                    i_new = i + dx
                    j_new = j + dy
                    if i_new < 0 or i_new >= n or j_new < 0 or j_new >= m or grid[i_new][j_new] < inf:
                        continue
                    grid[i_new][j_new] = dist + 1
                    new_front.append((i_new, j_new))
            front = new_front
            dist += 1



        