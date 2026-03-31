class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for i in range(len(s)):
            c = s[i]
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        for i in range(len(t)):
            c = t[i]
            if c not in counts:
                return False
            counts[c] -= 1
        for c in counts:
            if counts[c] != 0:
                return False
        return True
            