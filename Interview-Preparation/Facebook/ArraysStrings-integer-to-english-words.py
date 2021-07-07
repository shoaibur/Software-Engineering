class Solution:
    def numberToWords(self, num: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        if not num: return 'Zero'
        
        onedigit = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        twodigits_10to19 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
        
        def one(num):
            # if not num: return ''
            return onedigit[num]
        
        def two(num):
            # if not num: return ''
            if num < 10: return one(num)
            elif num < 20: return twodigits_10to19[num]
            else:
                _ty, rest = divmod(num, 10)
                return tens[_ty] + ' ' + one(rest) if rest else tens[_ty]
        
        def three(num):
            # if not num: return ''
            hundred, rest = divmod(num, 100)
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
            elif not hundred and rest:
                return two(rest)
        
        
        billions, rest = divmod(num, 1000000000)
        millions, rest = divmod(rest, 1000000)
        thousands, rest = divmod(rest, 1000)
        
        result = ''
        if billions:
            result += three(billions) + ' Billion'
        if millions:
            if result: result += ' '
            result += three(millions) + ' Million'
        if thousands:
            if result: result += ' '
            result += three(thousands) + ' Thousand'
        if rest:
            if result: result += ' '
            result += three(rest)
        return result
    
