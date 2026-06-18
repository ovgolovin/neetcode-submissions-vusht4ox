class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._prefix_sums = self._build_prefix_sums(matrix)  

    @staticmethod
    def _build_prefix_sums(matrix):
        m = len(matrix)
        n = len(matrix[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row_pref = 0
            for j in range(1, n + 1):
                row_pref += matrix[i - 1][j - 1]
                pref[i][j] = pref[i - 1][j] + row_pref
        return pref


        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self._prefix_sums[row2 + 1][col2 + 1]
            - self._prefix_sums[row1][col2 + 1]
            - self._prefix_sums[row2 + 1][col1]
            + self._prefix_sums[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)