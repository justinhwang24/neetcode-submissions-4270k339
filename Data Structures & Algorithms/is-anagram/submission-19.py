class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        if len(s) != len(t):
            return False
        for c in s:
            chars[ord(c) - ord('a')] += 1
        for c in t:
            chars[ord(c) - ord('a')] -= 1
        for c in chars:
            if c != 0:
                return False
        
        return True