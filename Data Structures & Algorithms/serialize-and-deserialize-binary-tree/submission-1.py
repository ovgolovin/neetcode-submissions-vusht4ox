# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                yield "N"
                return
            yield str(node.val)
            yield from dfs(node.left)
            yield from dfs(node.right)

        return ",".join(dfs(root))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            val = vals[i]
            i += 1
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

