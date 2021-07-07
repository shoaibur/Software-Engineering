class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        '''
        T: O(n) and S: O(1)
        '''
        chars = string.ascii_lowercase
        
        def getHighestChar(chars, n, k):
            for i in range(26, 0, -1):
                if k >= i and k - i >= n - 1:
                    k -= i
                    n -= 1
                    return chars[i-1], n, k
        s = ''
        while n > 0:
            char, n, k = getHighestChar(chars, n, k)
            s += char
            
        return s[::-1]
