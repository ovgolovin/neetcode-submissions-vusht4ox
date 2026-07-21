class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(count, char) for count, char in [(a, 'a'), (b, 'b'), (c, 'c')] if count > 0]
        heapq.heapify_max(heap)


        res = []

        while heap:
            count, char = heapq.heappop_max(heap)
            if len(res) > 1 and char == res[-1] == res[-2]:
                if not heap:
                    break
                count2, char2 = heapq.heappop_max(heap)
                res.append(char2)
                if count2 > 1:
                    heapq.heappush_max(heap, (count2 - 1, char2))
                heapq.heappush_max(heap, (count, char))
            else:
                res.append(char)
                if count > 1:
                    heapq.heappush_max(heap, (count - 1, char))

        return ''.join(res)
        