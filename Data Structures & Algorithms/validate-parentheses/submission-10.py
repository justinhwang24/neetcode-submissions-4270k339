class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in range(len(s)):
            if s[i] not in close_open:
                stack.append(s[i])
            if s[i] in close_open:
                if not stack:
                    return False
                if stack.pop() != close_open[s[i]]:
                    return False
        return not stack