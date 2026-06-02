from itertools import chain

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        if m < 2:
            return 
        n = len(board[0])
        if n < 2:
            return 

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque()

        for i, j in chain(
            ((i, j) for i in range(m) for j in [0, n - 1]),
            ((i, j) for i in [0, m - 1] for j in range(1, n - 1))):
                if board[i][j] == 'O':
                    q.append((i, j))
                    board[i][j] = 'B'

        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if ni < 1 or ni > m - 2 or nj < 1 or nj > n - 2 or board[ni][nj] != 'O':
                    continue
                board[ni][nj] = 'B'
                q.append((ni, nj))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'



        



        