class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        arr = []
        lens = []
        i = 0
        curr = ""
        while i < len(s) and s[i] != "#":
            if s[i] in "0123456789":
                curr += s[i]
            elif s[i] == ",":
                lens.append(int(curr))
                curr = ""
            i += 1
        i += 1
        for j in lens:
            word = ""
            for k in range(j):
                word += s[i]
                i += 1
            arr.append(word)
        return arr