class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindromeSubstring(s, i, j):
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i, j = i - 1, j + 1
            return s[i+1:j]
        
        palindrome = ''
        for i in range(len(s)):
            palindrome = max(palindrome, palindromeSubstring(s, i, i+1), palindromeSubstring(s, i-1, i+1), key=len)
        return palindrome
