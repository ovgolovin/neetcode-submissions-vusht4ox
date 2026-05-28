class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = [False] * n

        def bfs(start_node):
            queue = deque([start_node])
            visited[start_node] = True
            while queue:
                node = queue.popleft()
                for neigh in adj[node]:
                    if visited[neigh]:
                        continue
                    visited[neigh] = True
                    queue.append(neigh)

        
        res = 0
        for node in range(n):
            if visited[node]:
                continue
            bfs(node)
            res += 1

        return res
        