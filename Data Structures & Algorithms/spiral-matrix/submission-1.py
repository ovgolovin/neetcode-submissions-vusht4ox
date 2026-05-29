class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        res = []

        i = 0
        j = -1
        steps = [n, m - 1]
        di = 0
        dj = 1


        while steps[abs(di)] > 0:
            for _ in range(steps[abs(di)]):
                i += di
                j += dj
                res.append(matrix[i][j])
            steps[abs(di)] -= 1
            di, dj = dj, -di  # change direction clockwise

        return res

        