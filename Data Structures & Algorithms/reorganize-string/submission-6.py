class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(count, char) for char, count in counts.items()]
        heapq.heapify_max(heap)

        res = []
        prev = None
        
        while heap:
            count, char = heapq.heappop_max(heap)
            res.append(char)
            count -= 1

            if prev:
                heapq.heappush_max(heap, prev)
                prev = None

            if count > 0:
                prev = (count, char)
        if prev:
            return ""


        return ''.join(res)
        