class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
        
        # To get the repeating substring
        '''
        i = (s+s).find(s, 1, -1)
        repeatSub = s[:i]
        '''
        
        # Alternative solution
        '''
        for i in range(1,len(s)):
            subS = s[:i]
            ratio = len(s) // len(subS)
            if subS * ratio == s:
                return True
        return False
        '''
        
