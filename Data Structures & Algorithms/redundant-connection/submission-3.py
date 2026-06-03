class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.khan(edges)


    def khan(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] > 1 and indegree[v] > 1:
                return [u, v]
        return []


    def dfs(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        sentinel = object()
        stack = [(-1, 1)]
        visited = set()
        path = []
        while stack:
            item = stack.pop()
            if item is sentinel:
                path.pop()
                continue
            par, node = item
            if node in visited:
                cycle = set()
                for el in reversed(path):
                    cycle.add(el)
                    if el == node:
                        break
                break
            visited.add(node)
            path.append(node)
            stack.append(sentinel)
            for neigh in adj[node]:
                if par == neigh:
                    continue
                stack.append((node, neigh))
        
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]

        

        