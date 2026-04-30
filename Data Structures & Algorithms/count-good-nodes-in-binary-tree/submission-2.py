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
            node, path_max = stack.pop()
            if node.val >= path_max:
                res += 1
            new_path_max = max(path_max, node.val)
            if node.right:
                stack.append((node.right, new_path_max))
            if node.left:
                stack.append((node.left, new_path_max))       
        return res     
        