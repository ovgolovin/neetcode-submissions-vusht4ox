# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def postorder(root):
            node = root
            stack = []
            heights = []
            height = 0
            last_visited = None
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    peek = stack[-1]
                    if peek.right and peek.right != last_visited:
                        node = peek.right
                    else:
                        right = heights.pop() if peek.right else 0
                        left = heights.pop() if peek.left else 0
                        height = max(left, right) + 1
                        heights.append(height)
                        yield (peek, height)
                        last_visited = stack.pop()

        def are_trees_equal(a_root, b_root):
            stack = [(a_root, b_root)]
            while stack:
                a, b = stack.pop()
                if a is None and b is None:
                    continue
                if a is None or b is None:
                    return False
                if a.val != b.val:
                    return False
                stack.append((a.left, b.left))
                stack.append((a.right, b.right))
            return True

        for _, sub_height in postorder(subRoot):
            pass
        
        for node, height in postorder(root):
            if height == sub_height and are_trees_equal(node, subRoot):
                return True

        return False