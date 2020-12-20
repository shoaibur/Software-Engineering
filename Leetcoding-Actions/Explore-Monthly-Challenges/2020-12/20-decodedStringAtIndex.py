class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        '''
        T: O(n) and O(1)
        '''
        n = 0
        for char in S:
            if char.isdigit():
                n *= int(char)
            else:
                n += 1
        
        for char in S[::-1]:
            K = K % n
            if K == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                n = n / int(char)
            else:
                n -= 1
