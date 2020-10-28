class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        T: O(max(m, n)) and S: O(1)
        '''
        str2digit = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        digit2str = {val: key for key, val in str2digit.items()}
                
        n1, n2 = len(num1), len(num2)
        result = ''
        
        i, j, carry = n1 - 1, n2 - 1, 0
        while i >= 0 or j >= 0 or carry:
            v1 = num1[i] if i >= 0 else '0'
            v2 = num2[j] if j >= 0 else '0'
            
            v1, v2 = str2digit[v1], str2digit[v2]
            
            s = v1 + v2 + carry
            carry, s = divmod(s, 10)
            
            result += digit2str[s]
            
            i, j = i - 1, j - 1
        
        return result[::-1]
