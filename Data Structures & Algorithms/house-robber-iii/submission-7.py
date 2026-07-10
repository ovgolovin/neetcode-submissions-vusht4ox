# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from dataclasses import dataclass

@dataclass
class Result:
    including: int = 0
    excluding: int = 0

    @property
    def best(self):
        return max(self.including, self.excluding)


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Result:
            if not node:
                return Result(0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return Result(
                including = node.val + left.excluding + right.excluding,
                excluding = left.best + right.best
            )
            
        return dfs(root).best