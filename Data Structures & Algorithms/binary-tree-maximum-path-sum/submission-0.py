# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        node = root
        sentinel = object()
        stack = []
        children_res = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
                if node is None:
                    children_res.append(0)    
            else:
                top = stack[-1]
                if top is sentinel:
                    stack.pop()
                    top = stack.pop()
                    right = max(children_res.pop(), 0)
                    left = max(children_res.pop(), 0)
                    res = max(res, top.val + left + right)
                    children_res.append(top.val + max(left, right))
                else:
                    stack.append(sentinel)
                    node = top.right
                    if node is None:
                        children_res.append(0)                       
        return res