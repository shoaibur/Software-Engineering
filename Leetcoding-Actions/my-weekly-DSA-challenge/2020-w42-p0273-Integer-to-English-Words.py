class Solution:
    def numberToWords(self, num: int) -> str:
        '''
        T: O(log n)
        S: O(1)
        '''
        oneDigit = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
        twoDigits_10to19 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
        
        def one(num):
            return oneDigit[num]
        
        def two(num):
            if num < 10: return one(num)
            if num > 9 and num < 20: return twoDigits_10to19[num]
            ty, rem = divmod(num, 10)
            if rem:
                return tens[ty] + ' ' + one(rem)
            return tens[ty]
        
        def three(num):
            if num < 100: return two(num)
            hundred, rem = divmod(num, 100)
            if rem:
                remString = two(rem)
                return one(hundred) + ' Hundred ' + remString
            return one(hundred) + ' Hundred'
        

        if num == 0: return 'Zero'
        
        english = ''
        billion, num = divmod(num, 1000000000)
        if billion:
            space = ' ' if num else ''
            english += three(billion) + ' Billion' + space
        
        million, num = divmod(num, 1000000)
        if million:
            space = ' ' if num else ''
            english += three(million) + ' Million' + space
        
        thousand, num = divmod(num, 1000)
        if thousand:
            space = ' ' if num else ''
            english += three(thousand) + ' Thousand' + space
        
        if num:
            english += three(num)
        return english
