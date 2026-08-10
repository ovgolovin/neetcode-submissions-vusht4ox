class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        length = 1
        prev_sign = 0

        for i in range(len(arr) - 1):
            sign = (arr[i] < arr[i + 1]) - (arr[i] > arr[i + 1])

            if sign == 0:
                length = 1
            elif sign * prev_sign == -1:
                length += 1
            else:
                length = 2

            best = max(best, length)
            prev_sign = sign

        return best