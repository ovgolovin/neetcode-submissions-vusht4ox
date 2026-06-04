class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        best_times = [float("+inf")] * (n + 1)
        children = [{} for _ in range(n + 1)]
        for src, dst, time in times:
            children[src][dst] = min(children[src].get(dst, time), time)

        heap = [(0, k)]
        best_times[k] = 0
        max_time = 0
        visit_count = 0
        while heap:
            time, node = heapq.heappop(heap)
            if time > best_times[node]:
                continue
            visit_count += 1
            max_time = max(max_time, time)
            for child, dt in children[node].items():
                child_time = time + dt
                if child_time >= best_times[child]:
                    continue
                best_times[child] = child_time
                heapq.heappush(heap, (child_time, child))
        if visit_count < n:
            return -1
        return max_time

        