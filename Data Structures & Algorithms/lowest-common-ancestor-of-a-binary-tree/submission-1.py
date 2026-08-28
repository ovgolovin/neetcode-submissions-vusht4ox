class Solution:
    def lowestCommonAncestor(self, root, p, q):
        p_path = q_path = None
        path = []

        def dfs(node):
            nonlocal p_path, q_path
            if node is None or (p_path and q_path):
                return

            path.append(node)

            if node is p:
                p_path = path.copy()
            elif node is q:
                q_path = path.copy()

            if not (p_path and q_path):
                dfs(node.left)
            if not (p_path and q_path):
                dfs(node.right)

            path.pop()

        dfs(root)

        lca = None
        for a, b in zip(p_path, q_path):
            if a is not b:
                break
            lca = a
        return lca