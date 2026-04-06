class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortestLen = len(strs[0])
        for s in strs:
            shortestLen = min(shortestLen, len(s))
        curr = ""
        for i in range(shortestLen):
            last = strs[0][i]
            for s in strs:
                if s[i] != last:
                    return curr
            curr += last
        return curr