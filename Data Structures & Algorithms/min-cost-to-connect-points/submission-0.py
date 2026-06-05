class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n


    def find(self, i):
        par = self.parents[i]
        if par != i:
            par = self.parents[i] = self.find(par)
        return par


    def union(self, i, j):
        par1 = self.find(i)
        par2 = self.find(j)

        if par1 == par2:
            return 0

        if self.size[par1] < self.size[par2]:
            par1, par2 = par2, par1

        self.size[par1] += self.size[par2]
        self.parents[par2] = par1

        return self.size[par1]



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.kruskal(points)


    def kruskal(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append((dist, i, j))
        edges.sort()
        uf = UnionFind(n)
        total_dist = 0
        for dist, i, j in edges:
            join_size = uf.union(i, j)
            if join_size == 0:
                continue
            total_dist += dist
            if join_size == n:
                break

        return total_dist