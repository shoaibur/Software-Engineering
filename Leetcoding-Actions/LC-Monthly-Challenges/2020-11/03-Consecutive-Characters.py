class Solution:
    def maxPower(self, s: str) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        if len(s) == 1: return 1
        
        power = 0
        i, j = 0, 0
        while j < len(s):
            if s[i] == s[j]:
                j += 1
            else:
                i += 1
            power = max(power, j - i)
        
        return power
