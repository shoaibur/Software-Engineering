class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        T: O(n) and S: O(62) = O(1)
        '''
        if not s: return True
        
        chars = set(string.ascii_lowercase + string.ascii_uppercase + '0123456789')
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in chars and s[j] in chars:
                if s[i].lower() != s[j].lower():
                    return False
                i, j = i + 1, j - 1
            else:
                if s[i] not in chars:
                    i += 1
                if s[j] not in chars:
                    j -= 1
            
        return True
