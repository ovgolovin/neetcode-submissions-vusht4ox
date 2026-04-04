class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = n * m - 1
        while i <= j:
            mid = i + (j - i) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] > target:
                j = mid - 1
            elif matrix[row][col] < target:
                i = mid + 1
            else:
                return True
        return False