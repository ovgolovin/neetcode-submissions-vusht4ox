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

        stack = [root]
        visited = object()
        results = []

        while stack:
            if stack[-1] is visited:
                stack.pop()
                node = stack.pop()
                right = results.pop()
                left = results.pop()
                results.append((
                    max(left) + max(right),
                    left[0] + right[0] + node.val
                ))
            else:
                node = stack[-1]
                stack.append(visited)

                if node.left:
                    stack.append(node.left)
                else:
                    results.append((0,0))

                if node.right:
                    stack.append(node.right)
                else:
                    results.append((0,0))


        return max(results[0])


        