class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)

        res = []
        prev = None
        
        while heap:
            count, char = heapq.heappop(heap)
            res.append(char)
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count != 0:
                prev = (count, char)
        if prev:
            return ""


        return ''.join(res)
        