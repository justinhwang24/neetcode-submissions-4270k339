class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in close_open:
                stack.append(c)
            if c in close_open:
                if stack and stack[-1] == close_open[c]:
                    stack.pop()
                else:
                    return False
        return not stack