class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        def dfs(remaining, unclosed):
            if unclosed == 0 and remaining == 0:
                yield ''.join(stack)
                return
            if remaining > 0:
                stack.append('(')
                yield from dfs(remaining - 1, unclosed + 1)
                stack.pop()
            if unclosed > 0:
                stack.append(')')
                yield from dfs(remaining, unclosed - 1)
                stack.pop()


        return list(dfs(n, 0))
        