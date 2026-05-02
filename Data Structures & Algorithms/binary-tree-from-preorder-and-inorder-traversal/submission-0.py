# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from itertools import islice

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return []
        in_idx = 0
        root = TreeNode(preorder[0])
        stack = [root]
        for val in islice(preorder, 1, None):
            curr = stack[-1]
            node = TreeNode(val)
            if curr.val != inorder[in_idx]:
                curr.left = node
            else:
                while stack and stack[-1].val == inorder[in_idx]:
                    last = stack.pop()
                    in_idx += 1
                last.right = node
            stack.append(node)
        return root




