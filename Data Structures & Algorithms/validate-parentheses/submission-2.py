class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            prev_expected = closing_to_open.get(char)
            if prev_expected is not None:
                if not stack or stack[-1] != prev_expected:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0