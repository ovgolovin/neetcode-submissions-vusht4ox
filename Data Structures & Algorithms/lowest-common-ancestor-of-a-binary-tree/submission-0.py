# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = None
        q_path = None

        def dfs(path):
            nonlocal p_path
            nonlocal q_path

            node = path[-1]
            if node is p:
                p_path = path
            elif node is q:
                q_path = path

            if p_path and q_path:
                return

            if node.left:
                dfs(path + [node.left])

            if p_path and q_path:
                return

            if node.right:
                dfs(path + [node.right])            


        dfs([root])

        last_common = None
        for a, b in zip(p_path, q_path):
            if a is b:
                last_common = a

        return last_common
        