class Solution:
    def isPalindrome(self, s: str) -> bool:
        def to_lower_ord(c):
            o = ord(c)
            if ord('A') <= ord(c) <= ord('Z'):
                return o + ord('a') - ord('A')
            return o

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[right].isalnum():
                right -= 1
            while left < right and not s[left].isalnum():
                left += 1
            if left < right:
                if to_lower_ord(s[left]) != to_lower_ord(s[right]):
                    return False
                left += 1
                right -= 1
        return True   

