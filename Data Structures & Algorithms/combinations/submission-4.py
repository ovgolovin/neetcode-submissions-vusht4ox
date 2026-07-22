class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        comb = list(range(1, k + 1))

        index = k - 1  # position in combination

        while index >= 0:
            if comb[index] > n - k + index + 1:
                index -= 1
                if index >= 0:
                    comb[index] += 1
                continue

            if index == k - 1:
                results.append(comb[:])
                comb[index] += 1
                continue

            index += 1
            comb[index] = comb[index - 1] + 1

        return results
        