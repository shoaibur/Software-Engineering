class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        T: O(n^2) and S: O(1)
        '''
        def palindrome(s, i, j):
            while i >= 0 and j <= len(s) - 1:
                if s[i] != s[j]:
                    break
                i, j = i - 1, j + 1
            return s[i+1:j]
        
        result = ""
        for i in range(len(s)):
            result = max(result, palindrome(s, i-1, i+1), palindrome(s, i, i+1), key=len)
        
        return result
