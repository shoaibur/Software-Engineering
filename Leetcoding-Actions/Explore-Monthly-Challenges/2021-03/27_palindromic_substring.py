class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        T: O(n^2) and S: O(1)
        '''
        def count_palindrome(s, i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
                count += 1
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += count_palindrome(s, i, i)
            ans += count_palindrome(s, i, i+1)
        
        return ans
