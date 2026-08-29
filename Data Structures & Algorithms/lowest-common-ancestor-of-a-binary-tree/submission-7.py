class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_found = False
        q_found = False
        lca = None

        def dfs(node):
            nonlocal lca, p_found, q_found

            result = [False, False]

            if node is None:
                return result
            
            if lca:
                return result

            if node is p:
                result[0] = True
                p_found = True

            if node is q:
                result[1] = True
                q_found = True

            if p_found and q_found:
                return result

            for child in [node.left, node.right]:
                child_result = dfs(child)

                if lca:
                    return result

                result[0] |= child_result[0]
                result[1] |= child_result[1]
                
                if result[0] and result[1]:
                    lca = node
    
                if p_found and q_found:
                    return result

            return result


        dfs(root)

        return lca