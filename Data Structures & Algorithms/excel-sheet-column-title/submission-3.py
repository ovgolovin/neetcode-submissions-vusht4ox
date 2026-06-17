class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        div = columnNumber
        while div:
            div, rem = divmod(div - 1, 26)
            res.append(chr(ord('A') + rem))
        return ''.join(reversed(res))
        