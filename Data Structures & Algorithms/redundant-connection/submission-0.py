class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [set() for _ in range(n + 1)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

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

        

        