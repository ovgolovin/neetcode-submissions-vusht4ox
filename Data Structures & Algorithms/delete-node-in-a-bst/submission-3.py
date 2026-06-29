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

        par = dummy = TreeNode(left=root)
        curr = root
        while True:
            if not curr:
                return root
            elif key == curr.val:
                break
            elif key < curr.val:
                par = curr
                curr = curr.left
            else:
                par = curr
                curr = curr.right

        if not curr.left or not curr.right:
            child = curr.left or curr.right
            if par.left is curr:
                par.left = child
            else:
                par.right = child
            return dummy.left

        

        tmp = curr.right
        tmp_par = None
        while tmp.left:
            tmp_par = tmp
            tmp = tmp.left
        
        if tmp_par:
            tmp_par.left = tmp.right
            tmp.right = curr.right

        tmp.left = curr.left

        if par.left is curr:
            par.left = tmp
        else:
            par.right = tmp            

        return dummy.left
        