class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p = max( p, self.palindrome(s, i, i+1), self.palindrome(s, i-1, i+1), key=len )
        return p
    
    def palindrome(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i, j = i-1, j+1
        return s[i+1:j]
