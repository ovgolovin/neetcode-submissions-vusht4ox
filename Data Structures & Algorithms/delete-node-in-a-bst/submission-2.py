# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = dummy = TreeNode(float("inf"), left=root)
        curr = root
        while True:
            if not curr:
                return root
            elif key == curr.val:
                break
            elif key < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        if not curr.left or not curr.right:
            child = curr.left or curr.right
            if prev.val > key:
                prev.left = child
            else:
                prev.right = child
            return dummy.left

        

        tmp = curr.right
        tmp_par = curr
        while tmp.left:
            tmp_par = tmp
            tmp = tmp.left
        
        if tmp.right:
            cand = tmp.right
        else:
            cand = None
        if tmp_par.left is tmp:
            tmp_par.left = cand
        else:
            tmp_par.right = cand
        
        curr.val = tmp.val
            


        return dummy.left
        