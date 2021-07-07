class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValid(s):
            return s == s[::-1]
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return isValid(s[i:j]) or isValid(s[i+1:j+1])
            i, j = i + 1, j - 1
        return True
