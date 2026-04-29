# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        node = root
        max_diam = 0
        last_visited = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != last_visited:
                    node = peek.right
                else:
                    left = peek.left.height if peek.left else 0
                    right = peek.right.height if peek.right else 0
                    peek.height = max(left, right) + 1
                    max_diam = max(max_diam, left + right)
                    last_visited = stack.pop()
        return max_diam



        