class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        curr1 = 0
        curr2 = 0
        while curr1 < len(word1) and curr2 < len(word2):
            res += word1[curr1]
            res += word2[curr2]
            curr1 += 1
            curr2 += 1
        if curr1 < len(word1):
            res += word1[curr1:]
        if curr2 < len(word2):
            res += word2[curr1:]
        return res