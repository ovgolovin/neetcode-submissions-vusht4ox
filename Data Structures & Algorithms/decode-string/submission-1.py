class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        factor = 0
        for char in s:
            res = ""
            if ord('0') <= ord(char) <= ord('9'):
                factor = 10 * factor + (ord(char) - ord('0'))
            elif char == '[':
                stack.append(factor)
                factor = 0
            elif char == "]":
                substr = stack.pop()
                mult = stack.pop()
                res = substr * mult
            else:
                res = char

            if stack and type(stack[-1]) is str:
                stack[-1] = stack[-1] + res
            else:
                stack.append(res)

        return stack[0]


        