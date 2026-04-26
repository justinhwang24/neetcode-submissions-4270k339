class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValidPalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for i in range(len(s)):
            if isValidPalindrome(s[:i] + s[i + 1:]):
                return True
        return False