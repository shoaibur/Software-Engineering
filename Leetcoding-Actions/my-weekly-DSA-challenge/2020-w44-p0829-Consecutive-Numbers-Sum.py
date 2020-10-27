class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        N = (x + 1) + (x + 2) + ... + (x + k)
          = xk + 1 + 2 + ... + k
          = xk + k(k + 1) / 2
        x = N / k - (k + 1) / 2
        x >= 0 and x is integer
        For x >= 0:
        N / k >= (k + 1) / 2
        k <= sqrt(2N + 1/4) - 1/2
        
        T: O(sqrt(N)) and S: O(1)
        '''
        count = 0
        maxK = int((2 * N + 0.25)**0.5 - 0.5)
        
        for k in range(1, maxK + 1):
            x = N / k - (k + 1) / 2
            if x % 1 == 0:
                count += 1
        return count
            
        
        
        
        '''
        # Brute-force solution:
        # T: O(n) and S: O(1)
        count = 1
        i, j = 1, 2
        curSum = i
        while j < N/2:
            if curSum == N:
                count += 1
                curSum -= i
                i += 1
            elif curSum < N:
                curSum = curSum + j
                j += 1
            else:
                curSum -= i
                i += 1
        return count
        '''
