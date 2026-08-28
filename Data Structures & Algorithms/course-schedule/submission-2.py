class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0

        while queue:
            curr = queue.popleft()
            taken += 1

            for nxt in adj[curr]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    queue.append(nxt)

        return taken == numCourses


        