from dataclasses import dataclass

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def height(node):
            nonlocal max_diam
            if node is None:
                return 0
            l_height = height(node.left)
            r_height = height(node.right)
            max_diam = max(max_diam, l_height + r_height)
            return max(l_height, r_height) + 1
        
        height(root)
        return max_diam