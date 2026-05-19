from pprint import pprint

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        if n == 0:
            return
        m = len(grid[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1 ,0)]

        front = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    front.add((i, j))

        dist = 0
        while front:
            new_front = set()
            for i, j in front:
                grid[i][j] = dist
                for dx, dy in moves:
                    i_new = i + dx
                    j_new = j + dy
                    if i_new < 0 or i_new >= n or j_new < 0 or j_new >= m or grid[i_new][j_new] == -1 or grid[i_new][j_new] < 2147483647 or (i_new, j_new) in new_front or (i_new, j_new) in front:
                        continue
                    new_front.add((i_new, j_new))
            front = new_front
            dist += 1



        