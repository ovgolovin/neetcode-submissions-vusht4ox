class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_set = set(closing_to_open.values())
        for char in s:
            if char in open_set:
                stack.append(char)
                continue
            prev_expected = closing_to_open.get(char, None)
            if prev_expected is not None:
                if not stack or stack[-1] != prev_expected:
                    return False
                stack.pop()
        return len(stack) == 0