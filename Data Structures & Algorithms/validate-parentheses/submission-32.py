class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if stack and c in mp.keys() and mp[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return not stack