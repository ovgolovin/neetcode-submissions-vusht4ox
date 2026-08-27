class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            indegree[src] += 1
            indegree[dst] += 1

        leaves = deque([i for i in range(n) if indegree[i] == 1])
        remain_nodes = n


        while leaves:
            if remain_nodes <= 2:
                return list(leaves)

            remain_nodes -= len(leaves)

            for _ in range(len(leaves)):
                node = leaves.popleft()

                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        leaves.append(nei)


        