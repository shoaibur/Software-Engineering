class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        rom2int = {'M':1000, 
                   'CM':900, 
                   'D':500, 
                   'CD':400, 
                   'C':100, 
                   'XC':90, 
                   'L':50, 
                   'XL':40, 
                   'X':10, 
                   'IX':9, 
                   'V':5, 
                   'IV':4, 
                   'I':1,
                  }
        
        result = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in rom2int:
                key = s[i:i+2]
                i += 2
            elif s[i] in rom2int:
                key = s[i]
                i += 1
            result += rom2int[key]
        return result
