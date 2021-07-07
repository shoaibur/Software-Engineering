class Solution:
    def intToRoman(self, num: int) -> str:
        maps = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 5:'V', 4:'IV', 1:'I'}
        integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        out = ''
        i = 0
        
        while num > 0:
            s, num = divmod(num, integer[i])
            out += roman[i]*s
            if num < integer[i]:
                i += 1
        return out
