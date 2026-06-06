class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c
        l = 0
        r = len(newS) - 1
        while l <= r:
            if newS[l].lower() != newS[r].lower():
                return False
            l += 1
            r -= 1
        return True