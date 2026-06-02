from pprint import pprint

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def is_boundary(i, j):
            return i == 0 or i == m - 1 or j == 0 or j == n - 1


        for start_i in range(m):
            for start_j in range(n):
                if board[start_i][start_j] != 'O':
                    continue
                is_surrounded = not is_boundary(start_i, start_j)
                visited = set([(start_i, start_j)])
                queue = deque(visited)
                while queue:
                    i, j = queue.popleft()
                    di, dj = 1, 0
                    for _ in range(4):
                        ni = i + di
                        nj = j + dj
                        di, dj = dj, -di
                        if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or board[ni][nj] != 'O' or (ni, nj) in visited:
                            continue
                        visited.add((ni, nj))
                        queue.append((ni, nj))
                        is_surrounded = is_surrounded and not is_boundary(ni, nj)
                for ni, nj in visited:
                    board[ni][nj] = 'X' if is_surrounded else 'B'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'B':
                    board[i][j] = 'O'


        