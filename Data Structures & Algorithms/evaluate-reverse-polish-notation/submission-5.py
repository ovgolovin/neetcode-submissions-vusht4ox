class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                right, left = (stack.pop(), stack.pop())
                stack.append(left - right)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                right, left = (stack.pop(), stack.pop())
                stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack[0]