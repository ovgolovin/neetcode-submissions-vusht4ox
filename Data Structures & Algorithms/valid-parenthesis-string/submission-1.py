class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for char in s:
            if char == '(':
                lo += 1
                hi += 1
            elif char == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1
                hi += 1
            
            if hi < 0:
                return False
            lo = max(0, lo)
        return lo <= 0
        