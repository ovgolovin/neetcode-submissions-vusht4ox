class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited1 = [['N'] * n for _ in range(m)]
        visited1[0][0] = 'F'
        front1 = [(grid[0][0], 0, 0)]
        front2 = [(grid[m-1][n-1], m-1, n-1)]
        visited2 = [['N'] * n for _ in range(m)]
        visited2[m-1][n-1] = 'F'
        res = 0

        while front1 and front2:
            if len(front1) > len(front2):
                front1, front2 = front2, front1
                visited1, visited2 = visited2, visited1

            cost, i, j = heapq.heappop(front1)
            print(cost, i, j)
            if visited1[i][j] == 'V':
                continue
            res = max(res, cost)
            visited1[i][j] = 'V'
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or visited1[ni][nj] != 'N':
                    continue
                if visited2[ni][nj] == 'V':
                    return res
                visited1[ni][nj] = 'F'
                heapq.heappush(front1, (grid[ni][nj], ni, nj))
            
        