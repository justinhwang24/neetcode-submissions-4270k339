class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charS = [0] * 26
        for c in s:
            charS[ord(c) - ord('a')] += 1
        for c in t:
            charS[ord(c) - ord('a')] -= 1
        for i in charS:
            if i != 0:
                return False
        return True
        