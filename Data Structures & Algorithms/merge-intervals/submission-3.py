class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(interval[0] for interval in intervals)

        ends = [None] * (max_start + 1)
        for start, end in intervals:
            ends[start] = end if ends[start] is None else max(ends[start], end)

        res = []
        curr_start = None
        curr_end = None
        for start, end in enumerate(ends):
            if end is not None:
                curr_start = start if curr_start is None else curr_start
                curr_end = end if curr_end is None else max(curr_end, end)
            if curr_end == start:
                res.append([curr_start, curr_end])
                curr_start = None
                curr_end = None

        if curr_start is not None:
            res.append([curr_start, curr_end])

        return res