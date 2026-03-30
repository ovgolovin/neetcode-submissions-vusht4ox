class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanum(char):
            return (ord('a') <= ord(char) <= ord('z')
                or ord('A') <= ord(char) <= ord('Z')
                or ord('0') <= ord(char) <= ord('9')
            )

        left = 0
        right = len(s) - 1
        while True:
            while left < right and not is_alphanum(s[right]):
                right -= 1
            while left < right and not is_alphanum(s[left]):
                left += 1
            if left >= right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
                