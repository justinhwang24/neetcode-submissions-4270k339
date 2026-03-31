class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countsS = {}
        countsT = {}
        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]
            countsS[c_s] = 1 + countsS.get(c_s, 0)
            countsT[c_t] = 1 + countsT.get(c_t, 0)
        return countsS == countsT
            