class Solution:
    def isHappy(self, n: int) -> bool:
        def squares_sum(x):
            res = 0
            while x:
                res += (x % 10) ** 2
                x //= 10
            return res

        slow = n
        fast = squares_sum(n)
        while slow != fast and fast != 1:
            slow = squares_sum(slow)
            fast = squares_sum(fast)
            fast = squares_sum(fast)

        return fast == 1
        