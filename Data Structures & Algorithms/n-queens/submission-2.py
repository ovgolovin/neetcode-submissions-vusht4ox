class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = 0
        pos_diag = 0
        neg_diag = 0  
        board = []


        def switch_occupied(i, j):
            nonlocal cols, pos_diag, neg_diag
            cols ^= 1 << j
            pos_diag ^= 1 << (i + j)
            neg_diag ^= 1 << (i - j + n)

        def is_occupied(i, j):
            nonlocal cols, pos_diag, neg_diag
            return (cols & 1 << j) or (pos_diag & 1 << (i + j)) or (neg_diag & 1 << (i - j + n))

        def dfs(i):
            nonlocal cols, pos_diag, neg_diag
            if i == n:
                yield [''.join('Q' if j == col else '.' for j in range(n)) for col in board]
                return
            
            for j in range(n):
                if is_occupied(i, j):
                    continue
    
                switch_occupied(i, j)
                board.append(j)
                yield from dfs(i + 1)
                switch_occupied(i, j)
                board.pop()

        return list(dfs(0))