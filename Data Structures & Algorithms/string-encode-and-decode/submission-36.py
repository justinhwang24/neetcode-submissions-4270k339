class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            count = int(count)
            i += 1
            j = i + count
            res.append(s[i:j])
            i = j
        return res
