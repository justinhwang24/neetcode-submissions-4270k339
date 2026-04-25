class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = [0] * 26
        charT = [0] * 26
        for c in s:
            charS[ord(c) - ord('a')] += 1
        for c in t:
            charT[ord(c) - ord('a')] += 1
        return charS == charT