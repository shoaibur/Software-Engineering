class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        integer = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in maps:
                num = maps[s[i:i+2]]
                i += 2
            elif s[i] in maps:
                num = maps[s[i]]
                i += 1
            else: return 0
            integer += num
            
        return integer
