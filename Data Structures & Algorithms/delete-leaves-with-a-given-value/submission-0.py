# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = TreeNode(left=root)

        def dfs(node):
            if node is None:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.left or node.right:
                return node
            elif node.val == target:
                return None
            else:
                return node


        dfs(dummy)

        return dummy.left
                

        