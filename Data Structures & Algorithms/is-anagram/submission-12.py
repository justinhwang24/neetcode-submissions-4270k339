class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for c in s:
            num = ord(c) - ord('a')
            letters[num] = 1 + letters.get(num, 0)
        for c in t:
            num = ord(c) - ord('a')
            if num not in letters or not letters[num]:
                return False
            letters[num] -= 1
            if not letters[num]:
                letters.pop(num)
        return not letters