class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        res = []

        left = 0
        right = n
        top = 0
        bottom = m


        while True:
            if left >= right:
                break
            for j in range(left, right):
                res.append(matrix[top][j])
            top += 1

            if top >= bottom:
                break
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if left >= right:
                break
            for j in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][j])
            bottom -= 1

            if top >= bottom:
                break
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

        