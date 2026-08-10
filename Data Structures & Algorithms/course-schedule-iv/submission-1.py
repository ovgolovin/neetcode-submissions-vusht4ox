class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        adj = [set() for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].add(dst)

        ancestors = [set() for _ in range(numCourses)]

        queue = deque((i for i in range(numCourses) if indegree[i] == 0))

        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])

        return [src in ancestors[dst] for src, dst in queries]