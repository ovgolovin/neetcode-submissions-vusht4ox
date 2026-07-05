class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        ordered = sorted((start, duration, i) for i, (start, duration) in enumerate(tasks))


        ready = []
        ordered_next_idx = 0
        res = []
        end = 0
        while ready or ordered_next_idx < n:
            if not ready:
                end = max(end, ordered[ordered_next_idx][0])

            while ordered_next_idx < n and ordered[ordered_next_idx][0] <= end:
                start, duration, orig_idx  = ordered[ordered_next_idx]
                heapq.heappush(ready, (duration, orig_idx))
                ordered_next_idx += 1

            duration, orig_idx = heapq.heappop(ready)
            res.append(orig_idx)
            end += duration

        return res

        


        