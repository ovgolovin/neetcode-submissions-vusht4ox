class Solution:
    def climbStairs(self, n: int) -> int:
        return self.matrix(n)



    def matrix(self, n: int) -> int:
        def mult(a, b):
            return [[sum(a[i][x] * b[x][j] for x in range(len(a[0]))) for j in range(len(a[0]))] for i in range(len(a))]

        base = [
            [1, 1],
            [1, 0],
        ]

        res = [
            [1, 0],
            [0, 1],
        ]

        while n:
            if n % 2:
                res = mult(res, base)
            base = mult(base, base)
            n //= 2

        return res[0][0]



    def iterative(self, n: int) -> int:
        # O(n)

        prev = 1
        curr = 1

        for i in range(n - 1):
            prev, curr = curr, prev + curr

        return curr
        