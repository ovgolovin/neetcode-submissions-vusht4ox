class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        res = []

        i = 0
        j = -1  # start from dummy column position (which is incremented first)
        steps = [n, m - 1]   # [next available horisontal steps, next available vertical steps]
        di = 0  # increments for right direction
        dj = 1


        while steps[abs(di)] > 0:
            for _ in range(steps[abs(di)]):
                i += di
                j += dj
                res.append(matrix[i][j])
            steps[abs(di)] -= 1  # one less step in the opposite direction
            di, dj = dj, -di  # change direction clockwise

        return res

        