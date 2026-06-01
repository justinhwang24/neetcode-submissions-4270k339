class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if stack and c in pMap.keys() and stack[-1] == pMap[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack
