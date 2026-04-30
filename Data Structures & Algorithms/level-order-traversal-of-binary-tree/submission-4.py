# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cur = [root] if root is not None else []
        while cur:
            nxt = []
            level = []
            for node in cur:
                level.append(node.val)
                if node.left is not None:
                    nxt.append(node.left)
                if node.right is not None:
                    nxt.append(node.right)
            res.append(level)
            cur = nxt
        return res




        