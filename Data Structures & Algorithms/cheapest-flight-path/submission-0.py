class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("+inf")] * n
        costs[src] = 0
        adj = [[] for _ in range(n)]
        for i, j, cost in flights:
            adj[i].append((j, cost))

        queue = deque([(0, src, 0)])  # [(price, node, legs)]

        while queue:
            cost, node, legs = queue.popleft()

            for nei, leg_cost in adj[node]:
                nei_cost = cost + leg_cost
                if nei_cost >= costs[nei]:
                    continue
                costs[nei] = nei_cost
                if legs < k:
                    queue.append((nei_cost, nei, legs + 1))

        return costs[dst] if costs[dst] < float("+inf") else -1
        