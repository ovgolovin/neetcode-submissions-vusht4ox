# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.morris_traversal(root, k)

    
    def morris_traversal(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right





        
    def dfs_iterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                curr = stack.pop()
                k -= 1
                if k == 0:
                    return curr.val
                node = curr.right