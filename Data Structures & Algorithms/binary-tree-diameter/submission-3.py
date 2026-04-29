# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        heights = []
        sentinel = object()
        max_diam = 0
        while stack:
            node = stack.pop()
            if node is None:
                heights.append(0)
            elif node is sentinel:
                left = heights.pop()
                right = heights.pop()
                max_diam = max(max_diam, left + right)
                heights.append(max(left, right) + 1)
            else:
                stack.append(sentinel)
                stack.append(node.right)
                stack.append(node.left)
        return max_diam



        