"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        leaves = [
            Node(0, True),
            Node(1, True)
        ]


        def dfs(n, i, j):
            if n == 1:
                return leaves[grid[i][j]]


            half = n // 2
            children = [
                dfs(half, i, j),
                dfs(half, i, j + half),
                dfs(half, i + half, j),
                dfs(half, i + half, j + half)
            ]

            if (all(child.isLeaf for child in children)
                and all(children[0].val == children[i].val for i in range(1, 4))):
                return children[0]

            return Node(0, False, *children)
        
        return dfs(len(grid), 0, 0)