class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        i = 1
        factorCount = 0
        while i <= n:
            if n % i == 0:
                factorCount += 1
            if factorCount == k:
                break
            i += 1
        
        return i if factorCount == k else -1
