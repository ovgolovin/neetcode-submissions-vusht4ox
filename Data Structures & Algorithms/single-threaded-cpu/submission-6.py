class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        task_order = sorted(range(n), key=lambda i: tasks[i][0])

        next_task = 0
        ready = []
        res = []
        end_time = 0
        while next_task < n or ready:
            if not ready:
                end_time = max(end_time, tasks[task_order[next_task]][0])

            while next_task < n and (tasks[task_order[next_task]][0] <= end_time):
                task_idx = task_order[next_task]
                enqueue_time, processing_time = tasks[task_idx]
                heapq.heappush(ready, (processing_time, task_idx))
                next_task += 1

            processing_time, task_idx = heapq.heappop(ready)
            res.append(task_idx)
            end_time = end_time + processing_time

        return res


        