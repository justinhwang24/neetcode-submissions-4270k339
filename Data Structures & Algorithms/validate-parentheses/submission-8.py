class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            if s[i] in [')', '}', ']']:
                if not stack:
                    return False
                if stack.pop() != d[s[i]]:
                    return False
        return not stack