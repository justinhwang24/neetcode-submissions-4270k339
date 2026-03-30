class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in close_open:
                if not stack or stack.pop() != close_open.get(c):
                    return False
            else:
                stack.append(c)
        return not stack