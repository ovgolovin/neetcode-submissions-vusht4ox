class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        if n == 0:
            return
        m = len(grid[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1 ,0)]

        queue = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = dist
                for dx, dy in moves:
                    i_new = i + dx
                    j_new = j + dy
                    if i_new < 0 or i_new >= n or j_new < 0 or j_new >= m or (i_new, j_new) in visited or grid[i_new][j_new] == -1:
                        continue
                    queue.append((i_new, j_new))
                    visited.add((i_new, j_new))
            dist += 1



        