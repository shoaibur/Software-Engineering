class Solution:    
    def multiply(self, num1: str, num2: str) -> str:
        
        def convertStr2Num(s):
            result = 0
            k = 0
            for i in range(len(s)-1,-1,-1):
                result += int(s[i]) * 10**k
                k += 1
            return result
    
        num1 = convertStr2Num(num1)
        num2 = convertStr2Num(num2)
        
        return str(num1 * num2)
    
# Solution 2: without using int or srt functions directly
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str2num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        num2str = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
        
        def str2int(s):
            result = 0
            s = s[::-1]
            for i in range(len(s)):
                result += str2num[s[i]] * 10**i
            return result
        
        product = str2int(num1) * str2int(num2)
        
        if product == 0:
            return num2str[product]
        
        productStr = ''
        while product:
            product, rem = divmod(product, 10)
            productStr += num2str[rem]
        return productStr[::-1]
