class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        res = 0
        sign = 0

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                count = count + 1 if sign == 1 else 1
                sign = -1
            elif arr[i] < arr[i + 1]:
                count = count + 1 if sign == -1 else 1
                sign = +1
            else:  # equal
                count = 0
                sign = 0

            res = max(res, count)

        return res + 1
        