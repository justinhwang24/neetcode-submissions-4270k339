class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charS = [0] * 26
        for i in range(len(s)):
            charS[ord(s[i]) - ord('a')] += 1
            charS[ord(t[i]) - ord('a')] -= 1
        for i in charS:
            if i != 0:
                return False
        return True
        