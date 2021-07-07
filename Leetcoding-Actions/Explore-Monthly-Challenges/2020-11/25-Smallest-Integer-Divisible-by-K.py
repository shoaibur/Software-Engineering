class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        '''
        T: O(K) and S: O(1)
        '''
        remainder = 0
        
        for lengthN in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            
            if remainder == 0:
                return lengthN
        
        return -1
            
            
