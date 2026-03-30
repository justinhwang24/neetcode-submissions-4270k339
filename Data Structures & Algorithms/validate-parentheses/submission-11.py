class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in close_open:
                stack.append(c)
            if c in close_open:
                if not stack:
                    return False
                if stack.pop() != close_open[c]:
                    return False
        return not stack