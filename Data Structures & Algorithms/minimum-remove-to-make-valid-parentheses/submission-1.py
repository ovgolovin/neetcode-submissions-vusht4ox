class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        unused_close = s.count(')')
        opened = 0
        res = []
        for c in s:
            if c == "(":
                if opened == unused_close:
                    continue
                opened += 1
            elif c == ')':
                unused_close -= 1
                if opened == 0:
                    continue
                opened -= 1
            res.append(c)
        return ''.join(res)
        