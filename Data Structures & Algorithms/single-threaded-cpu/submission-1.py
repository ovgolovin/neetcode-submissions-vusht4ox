class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        task_order = sorted(range(len(tasks)), key=lambda i: tasks[i])

        next_task = 0
        ready = []
        res = []
        end_time = 0
        while next_task < n or ready:
            while next_task < n and (tasks[task_order[next_task]][0] <= end_time or not ready):
                task_idx = task_order[next_task]
                enqueue_time, processing_time = tasks[task_idx]
                heapq.heappush(ready, (processing_time, task_idx, enqueue_time))
                next_task += 1

            processing_time, task_idx, enqueue_time = heapq.heappop(ready)
            res.append(task_idx)
            if end_time <= enqueue_time:
                end_time = enqueue_time + processing_time
            else:
                end_time = end_time + processing_time

        return res


        