class Solution:
    def romanToInt(self, s: str) -> int:
        # integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        maps = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        summ = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in maps:
                key = s[i:i+2]
                i += 2
            elif s[i] in maps:
                key = s[i]
                i += 1
            summ += maps[key]
        return summ
