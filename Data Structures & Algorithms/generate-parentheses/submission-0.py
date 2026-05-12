class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(opened, closed, stack):
            if opened == closed == n:
                yield ''.join(stack)
                return

            if opened < n:
                stack.append("(")
                yield from dfs(opened + 1, closed, stack)
                stack.pop()
            if closed < opened:
                stack.append(")")
                yield from dfs(opened, closed + 1, stack)
                stack.pop()

        return list(dfs(0, 0, []))
        