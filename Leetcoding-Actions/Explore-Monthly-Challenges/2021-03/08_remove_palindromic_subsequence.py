class Solution:
    def removePalindromeSub(self, s: str) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        def is_palindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True
        
        if not s:
            return 0
        if is_palindrome(s):
            return 1
        return 2
