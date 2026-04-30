# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        if p.val > q.val:
            p, q = q, p
        while node:
            if p.val <= node.val <= q.val:
                return node
            elif q.val <= node.val:
                node = node.left
            else:
                node = node.right
        