class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in lastIndex:
                l = max(lastIndex[s[r]] + 1, l)
            lastIndex[s[r]] = r
            res = max(res, r - l + 1)
        return res