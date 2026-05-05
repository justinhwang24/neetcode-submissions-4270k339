class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        window = [0] * 26
        s1Arr = [0] * 26
        for c in s1:
            s1Arr[ord(c) - ord('a')] += 1
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if window == s1Arr:
                return True
        return False