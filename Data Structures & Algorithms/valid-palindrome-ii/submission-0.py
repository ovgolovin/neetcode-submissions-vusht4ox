class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r, can_delete=True):
            while l < r:
                if s[l] != s[r]:
                    if can_delete:
                        return is_palindrome(l + 1, r,  can_delete=False) or is_palindrome(l, r - 1,  can_delete=False)
                    else:
                        return False
                l += 1
                r -= 1
            return True
        return is_palindrome(0, len(s) - 1,  can_delete=True)
        