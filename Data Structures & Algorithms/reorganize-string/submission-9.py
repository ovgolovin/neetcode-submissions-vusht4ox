class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        most_frequent = max(counts.items(), key=lambda x: x[1])
        if most_frequent[1] > (len(s) + 1) // 2:
            return ""

        def chars_in_order():
            for _ in range(most_frequent[1]):
                yield most_frequent[0]

            for char, count in counts.items():
                if char == most_frequent[0]:
                    continue
                for _ in range(count):
                    yield char

        res = [None] * len(s)

        chars_iter = chars_in_order()
        for offset in (0, 1):
            for i in range(0 + offset, len(s), 2):
                res[i] = next(chars_iter)

        return ''.join(res)

        