class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)
        i = 0
        heap = []
        res = [-1] * len(queries)

        for query, idx in sorted(((query, idx) for idx, query in enumerate(queries))):
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res


        