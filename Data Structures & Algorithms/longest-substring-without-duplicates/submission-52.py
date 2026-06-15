class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            length = max(r - l + 1, length)
        return length