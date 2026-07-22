# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        if root is None:
            return None

        stack = [(root, False)]
        processed = []


        while stack:
            node, visited = stack.pop()
            if not visited:
                if node is None:
                    processed.append(None)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
            else:
                node.right = processed.pop()
                node.left = processed.pop()
                if node.left is None and node.right is None and node.val == target:
                    processed.append(None)
                else:
                    processed.append(node)         


        return processed[0]
                

        