class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s.isdigit() or \
            (len(s) > 1 and s[0] == '-' and s[1:].isdigit()):
                stack.append(s)
            else:
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
        return int(stack[-1])