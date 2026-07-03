class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]

        if n < 3:
            return t[n]

        
        nxt = sum(t)
        for i in range(3, n + 1):
            t[i % 3], nxt = nxt, nxt - t[i % 3] + nxt

        return t[n % 3]
        