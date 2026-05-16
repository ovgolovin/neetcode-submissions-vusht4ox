class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
        return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)
            
        