class Solution:
    def isPalindrome(self, s: str) -> bool:
        newWord = ""
        for c in s:
            if c.isalnum():
                newWord += c.lower()
        l = 0
        r = len(newWord) - 1
        while l <= r:
            if newWord[l] != newWord[r]:
                return False
            l += 1
            r -= 1
        return True