class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'][::-1]
        integer = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000][::-1]
        
        result = ''
        for i, den in enumerate(integer):
            carry, num = divmod(num, den)
            result += roman[i]*carry
        return result
