class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        pos_diag = [False] * 2 * n
        neg_diag = [False] * 2 * n

        def set_occupied(i, j, val):
            cols[j] = val
            pos_diag[i + j] = val
            neg_diag[i - j + n] = val

        def is_occupied(i, j):
            return cols[j] or pos_diag[i + j] or neg_diag[i - j + n]

        
        board = []

        def dfs(i):
            if i == n:
                yield [''.join('Q' if j == col else '.' for j in range(n)) for col in board]
                return
            
            for j in range(n):
                if is_occupied(i, j):
                    continue
    
                set_occupied(i, j, True)
                board.append(j)
                yield from dfs(i + 1)
                set_occupied(i, j, False)
                board.pop()


        
        return list(dfs(0))