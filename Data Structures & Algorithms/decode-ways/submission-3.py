class Solution:
    def numDecodings(self, s: str) -> int:

        prev = 1
        curr = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            if prev == 0 and curr == 0:
                break
            prev, curr = curr, prev * (1 if s[i-1] == '1' or s[i-1] == '2' and s[i] in "0123456" else 0) + curr * (0 if s[i] == '0' else 1)

        return curr

        