class Solution:
    def addDigits(self, num: int) -> int:
        ''' Solution 1
        while num > 9:
            num = sum([int(i) for i in str(num)])
        return num
        '''
        
        ''' Solution 2
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9
        '''
        
        # Solution 3
        return 1 + (num - 1) % 9 if num else 0
