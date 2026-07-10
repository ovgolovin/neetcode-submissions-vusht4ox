# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        results = []

        while stack:
            node, visited = stack.pop()
            if visited:
                left = results.pop() if node.left else (0, 0)
                right = results.pop() if node.right else (0, 0)
                results.append((
                    max(left) + max(right),
                    left[0] + right[0] + node.val
                ))
            else:
                stack.append((node, True))

                if node.left:
                    stack.append((node.left, False))

                if node.right:
                    stack.append((node.right, False))


        return max(results[0])


        