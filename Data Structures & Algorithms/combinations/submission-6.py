class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        comb = [0] * k
        pos = 0

        while pos >= 0:
            comb[pos] += 1

            if comb[pos] > n - k + pos + 1:
                pos -= 1
            elif pos == k - 1:
                results.append(comb[:])
            else:
                pos += 1
                comb[pos] = comb[pos - 1]

        return results