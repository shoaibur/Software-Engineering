class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        '''
        T: O(log Y) and S: O(1)
        '''
        operations = 0
        
        while X < Y:
            operations += 1
            if Y % 2:
                Y += 1
            else:
                Y //= 2
        
        return operations + X - Y
