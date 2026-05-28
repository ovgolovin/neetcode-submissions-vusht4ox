class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set([0])
        queue = deque([(0, None)])  # [(node, parent), ...]

        while queue:
            curr, parent = queue.popleft()
            for neigh in adj[curr]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False                
                visited.add(neigh)
                queue.append((neigh, curr))
        
        return len(visited) == n
        