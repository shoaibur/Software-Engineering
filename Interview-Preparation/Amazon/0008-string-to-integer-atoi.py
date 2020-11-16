class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.split()
        if len(str) == 0: return 0
        str = str[0]
        
        if str[0] not in '+-0123456789': return 0
        
        if str[0] == '-':
            str = str[1:]
            neg = True
        elif str[0] == '+':
            str = str[1:]
            neg = False
        else:
            neg = False
        
        nums = []
        for char in str:
            if char in '0123456789':
                nums.append(char)
            else:
                break
        if len(nums) == 0: return 0
        nums = int(''.join(nums))
        
        if neg:
            nums = -nums
        if nums < -2**31: return -2**31
        if nums > 2**31-1: return 2**31-1
        return nums
            
        
