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
        leafs = [
            Node(0, True),
            Node(1, True)
        ]


        def dfs(n, i, j):
            if n == 1:
                return leafs[grid[i][j]]


            n //= 2
            children = [
                dfs(n, i, j),
                dfs(n, i, j + n),
                dfs(n, i + n, j),
                dfs(n, i + n, j + n)
            ]

            if (all(child.isLeaf for child in children)
                and all(children[0] == children[i] for i in range(1, 4))):
                return children[0]

            return Node(0, False, *children)
        
        return dfs(len(grid), 0, 0)