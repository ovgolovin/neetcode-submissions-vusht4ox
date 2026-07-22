class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        comb = [0] * k
        pos = 0

        while pos >= 0:
            # Advance to the next candidate for this position.
            comb[pos] += 1

            max_value = n - k + pos + 1

            if comb[pos] > max_value:
                # This position is exhausted: backtrack.
                pos -= 1

            elif pos == k - 1:
                # Complete combination.
                results.append(comb[:])

            else:
                # Descend; the child begins just before its first valid value.
                pos += 1
                comb[pos] = comb[pos - 1]

        return results