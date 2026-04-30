# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cur = [root]
        while cur:
            nxt = []
            level = []
            for node in cur:
                if node is not None:
                    level.append(node.val)
                    nxt.append(node.left)
                    nxt.append(node.right)
            if level:
                res.append(level)
            cur = nxt
        return res




        