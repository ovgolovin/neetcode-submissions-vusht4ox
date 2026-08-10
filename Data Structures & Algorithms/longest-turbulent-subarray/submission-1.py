class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        res = 0
        prev = 0

        for i in range(n - 1):
            curr = (arr[i] < arr[i + 1]) - (arr[i] > arr[i + 1])
            count = count + 1 if curr * prev == -1 else 0 if curr == 0 else 1
            res = max(res, count)
            prev = curr

        return res + 1
        