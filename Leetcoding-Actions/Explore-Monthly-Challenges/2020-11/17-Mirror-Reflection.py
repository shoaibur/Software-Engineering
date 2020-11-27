class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        T: O(log p) and S: O(1)
        '''
        if q == 0: return 0;
        
        m, n = 1, 1
        while m * p != n * q:
            n += 1
            m = (n * q) // p
        
        if n % 2 == 0:
            return 2
        elif m % 2 != 0:
            return 1
        return 0
