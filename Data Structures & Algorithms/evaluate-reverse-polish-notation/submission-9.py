class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif s == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif s == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif s == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a / b))
            else:
                stack.append(int(s))
        return int(stack[0])