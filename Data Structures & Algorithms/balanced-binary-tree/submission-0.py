# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node = root
        stack = []
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
                    if abs(left - right) > 1:
                        return False
                    peek.height = max(left, right) + 1
                    last_visited = stack.pop()
        return True
        