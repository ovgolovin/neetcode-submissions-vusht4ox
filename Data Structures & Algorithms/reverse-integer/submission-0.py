class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            rem = -x
            overflow_max = 2**31
        else:
            sign = 1
            rem = x
            overflow_max = 2**31 - 1


        o_base, o_rem = divmod(overflow_max, 10)

        res = 0
        while rem:
            rem, digit = divmod(rem, 10)
            if res > o_base or res == o_base and digit > o_rem:
                return 0
            res = 10 * res + digit

        return sign * res