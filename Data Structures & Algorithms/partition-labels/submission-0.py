class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lasts = {}
        for i, char in enumerate(s):
            lasts[char] = i
        res = []
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, lasts[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
