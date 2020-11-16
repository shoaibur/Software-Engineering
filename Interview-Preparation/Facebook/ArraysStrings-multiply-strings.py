class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def str2int(s):
            num = 0
            for i in range(len(s)-1,-1,-1):
                num += int(s[i]) * 10**(len(s)-1-i)
            return num
        
        def int2str(num):
            s = []
            while num:
                num, digit = divmod(num, 10)
                s.append(str(digit))
            return ''.join(s[::-1])
        
        num1 = str2int(num1)
        num2 = str2int(num2)
        num = num1 * num2
        
        num = str(num)
        return num
    
        # return int2str(num)
