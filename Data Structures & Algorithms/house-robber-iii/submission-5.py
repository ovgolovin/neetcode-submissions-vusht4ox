# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        sys.setrecursionlimit(11000)


        if not root:
            return 0


        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right) 

            return (
                max(left) + max(right),
                left[0] + right[0] + node.val
            ) 


        return max(dfs(root))


        