class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in parMap:
                stack.append(parMap[c])
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        return not stack