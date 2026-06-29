# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        par = None
        curr = root
        while curr and curr.val != key:
            if key < curr.val:
                par = curr
                curr = curr.left
            else:
                par = curr
                curr = curr.right

        if not curr:
            return root

        if not curr.left or not curr.right:
            child = curr.left or curr.right
            if par is None:
                return child
            elif par.left is curr:
                par.left = child
            else:
                par.right = child
            return root

        
        succ = curr.right
        succ_par = None
        while succ.left:
            succ_par = succ
            succ = succ.left
        
        if succ_par:
            succ_par.left = succ.right
            succ.right = curr.right

        succ.left = curr.left

        if par is None:
            return succ
        elif par.left is curr:
            par.left = succ
        else:
            par.right = succ            

        return root
        