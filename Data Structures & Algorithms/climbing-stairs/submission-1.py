class Solution:
    def climbStairs(self, n: int) -> int:
        return self.iterative(n)


    def iterative(self, n: int) -> int:
        # O(n)
        
        prev = 1
        curr = 1

        for i in range(n - 1):
            prev, curr = curr, prev + curr

        return curr
        