class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = []

        for char in s:
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            elif char == '[':
                stack.append((cur_str, cur_num))
                cur_num = 0
                cur_str = []
            elif char == ']':
                prev_str, num = stack.pop()
                prev_str.append(''.join(cur_str) * num)
                cur_str = prev_str
            else:
                cur_str.append(char)

        return ''.join(cur_str)


        