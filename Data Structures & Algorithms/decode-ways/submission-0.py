class Solution:
    def numDecodings(self, s: str) -> int:
        valid_codes = set(str(i + 1) for i in range(ord('Z') - ord('A') + 1))
        prev = 1
        curr = 1 if s[0] in valid_codes else 0
        for i in range(1, len(s)):
            if prev == 0 and curr == 0:
                break
            prev, curr = curr, prev * (1 if s[i-1:i+1] in valid_codes else 0) + curr * (1 if s[i] in valid_codes else 0)

        return curr

        