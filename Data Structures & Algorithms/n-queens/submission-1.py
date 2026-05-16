class State:
    def __init__(self, n):
        self.cols = 0
        self.pos_diag = 0
        self.neg_diag = 0
        self.n = n

    def switch_occupied(self, i, j):
        self.cols ^= 1 << j
        self.pos_diag ^= 1 << (i + j)
        self.neg_diag ^= 1 << (i - j + self.n)

    def is_occupied(self, i, j):
        return (self.cols & 1 << j) or (self.pos_diag & 1 << (i + j)) or (self.neg_diag & 1 << (i - j + self.n))


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = State(n)    
        board = []

        def dfs(i):
            if i == n:
                yield [''.join('Q' if j == col else '.' for j in range(n)) for col in board]
                # yield 1
                return
            
            for j in range(n):
                if state.is_occupied(i, j):
                    continue
    
                state.switch_occupied(i, j)
                board.append(j)
                yield from dfs(i + 1)
                state.switch_occupied(i, j)
                board.pop()


        #return sum(dfs(0))
        return list(dfs(0))