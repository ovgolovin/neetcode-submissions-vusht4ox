class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        grid = [row[:] for row in grid]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        front = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    front.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        while front and fresh > 0:
            new_front = []
            for i, j in front:
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] != 1:
                        continue
                    grid[ni][nj] = 2
                    fresh -= 1
                    new_front.append((ni, nj))
            front = new_front
            minutes += 1
        if fresh != 0:
            return -1
        return minutes
