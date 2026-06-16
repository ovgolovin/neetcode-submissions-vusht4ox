class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(count, char) for char, count in counts.items()]
        heapq.heapify_max(heap)

        res = []

        curr = heapq.heappop_max(heap)
        while heap:
            nxt = heapq.heappop_max(heap)
            res.append(curr[1])
            if curr[0] > 1:
                heapq.heappush_max(heap, (curr[0] - 1, curr[1]))
            curr = nxt
        if curr[0] > 1:
            return ""
        res.append(curr[1])
        return ''.join(res)
        