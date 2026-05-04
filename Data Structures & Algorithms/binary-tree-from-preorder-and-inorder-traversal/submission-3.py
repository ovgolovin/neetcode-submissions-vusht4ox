# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from itertools import islice

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.iterative_morris(preorder, inorder)


    def iterative_morris(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return []
        root = TreeNode(preorder[0])
        curr = root
        in_idx = 0
        pre_idx = 1
        while pre_idx < len(preorder) or in_idx < len(inorder):       
            if pre_idx < len(preorder) and curr.val != inorder[in_idx]:
                curr.left = TreeNode(preorder[pre_idx], right=curr)
                curr = curr.left
                pre_idx += 1
            else:
                in_idx += 1
                while in_idx < len(inorder) and curr.right and curr.right.val == inorder[in_idx]:
                    nxt = curr.right
                    curr.right = None
                    curr = nxt
                    in_idx += 1
                node =  TreeNode(preorder[pre_idx], right=curr.right) if pre_idx < len(preorder) else None
                pre_idx += 1
                curr.right = node
                curr = curr.right
        return root


    def iterative_stack(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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




