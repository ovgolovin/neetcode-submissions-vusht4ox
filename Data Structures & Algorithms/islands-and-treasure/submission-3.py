class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        if n == 0:
            return
        m = len(grid[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1 ,0)]

        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if grid[i][j] != 0 and grid[i][j] <= dist:
                    continue
                grid[i][j] = dist
                for dx, dy in moves:
                    i_new = i + dx
                    j_new = j + dy
                    if i_new < 0 or i_new >= n or j_new < 0 or j_new >= m or grid[i_new][j_new] == -1 or grid[i_new][j_new] <= dist + 1:
                        continue
                    queue.append((i_new, j_new))
            dist += 1



        