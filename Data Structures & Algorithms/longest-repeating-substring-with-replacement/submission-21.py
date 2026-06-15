class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        longest = 0
        maxF = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxF = max(maxF, cnt[s[r]])
            while r - l + 1 - maxF > k:
                cnt[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest