class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(group):
            seen = set()
            for item in group:
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen.add(item)
            return True

        for row in board:
            if not check(row):
                return False
        
        for j in range(9):
            if not check((board[i][j] for i in range(9))):
                return False
        
        for x_offset in range(0, 7, 3):
            for y_offset in range(0, 7, 3):
                if not check(board[i][j] for i in range(x_offset, x_offset+3) for j in range(y_offset, y_offset+3)):
                    return False

        return True