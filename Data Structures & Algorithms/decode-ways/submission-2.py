class Solution:
    def numDecodings(self, s: str) -> int:
        def count_if_valid_code_single_at(i):
            return 0 if s[i] == '0' else 1

        def count_if_valid_code_double_at(i):
            return 1 if s[i] == '1' or s[i] == '2' and s[i+1] in "0123456" else 0

        prev = 1
        curr = count_if_valid_code_single_at(0)
        for i in range(1, len(s)):
            if prev == 0 and curr == 0:
                break
            prev, curr = curr, prev * count_if_valid_code_double_at(i-1) + curr * count_if_valid_code_single_at(i)

        return curr

        