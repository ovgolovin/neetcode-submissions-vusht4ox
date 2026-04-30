# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node is None:
                continue
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))
        return res




        