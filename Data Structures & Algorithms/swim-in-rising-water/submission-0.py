class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        front1 = [(grid[0][0], 0, 0)]
        visited1 = set()
        front2 = [(grid[m-1][n-1], m-1, n-1)]
        visited2 = set()
        res = 0

        while front1 and front2:
            if len(front1) > len(front2):
                front1, front2 = front2, front1
                visited1, visited2 = visited2, visited1

            cost, i, j = heapq.heappop(front1)
            print(cost, i, j)
            if (i, j) in visited1:
                continue
            res = max(res, cost)
            visited1.add((i, j))
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or (ni, nj) in visited1:
                    continue
                if (ni, nj) in visited2:
                    return res
                heapq.heappush(front1, (grid[ni][nj], ni, nj))
            
        