class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        for (a, b), val in zip(equations, values):
            adj[a].append((b, val))
            adj[b].append((a, 1.0 / val))

        def bfs(src, target):

            if src not in adj or target not in adj:
                return -1

            if src == target:
                return 1
            
            q = deque([(src, 1)])
            visit = set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                for nei, weight in adj[node]:
                    if nei not in visit:
                        if nei == target:
                            return w * weight
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]