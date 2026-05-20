class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = set()
        atlantic = set()

        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))

        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m - 1, j))


        def bfs(visited):
            front = deque(visited)
            while front:
                i, j = front.popleft()
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    if ni < 0 or nj < 0 or ni >= m or nj >= n or heights[ni][nj] < heights[i][j] or (ni, nj) in visited:
                        continue
                    visited.add((ni, nj))
                    front.append((ni, nj))
        
        bfs(pacific)
        bfs(atlantic)

        return [(i, j) for i in range(m) for j in range(n) if (i,j) in pacific and (i,j) in atlantic]