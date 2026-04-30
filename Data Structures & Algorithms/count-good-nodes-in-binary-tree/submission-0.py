# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, root.val)] if root else []
        while stack:
            node, high = stack.pop()
            if node.val >= high:
                res += 1
            if node.right:
                stack.append((node.right, max(high, node.val)))
            if node.left:
                stack.append((node.left, max(high, node.val)))       
        return res     
        