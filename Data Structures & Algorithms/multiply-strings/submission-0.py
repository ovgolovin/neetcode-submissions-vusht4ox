from itertools import dropwhile

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'


        mult = [0] * (len(num1) + len(num2))

        zero_offset = ord('0')

        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                mult[i + j] += (ord(c1) - zero_offset) * (ord(c2) - zero_offset)

        for i in range(len(mult) - 1):
            div, rem = divmod(mult[i], 10)
            mult[i + 1] += div
            mult[i] = rem

        mult.reverse()

        return ''.join(chr(digit + zero_offset) for digit in dropwhile(lambda x: x == 0, mult))
        