class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        n = len(A)
        if n < 3: return 0
        
        count = 0
        summ = 0
        for i in range(2, n):
            if (A[i] - A[i-1]) == (A[i-1] - A[i-2]):
                count += 1
            else:
                summ += (count + 1) * count // 2
                count = 0
        summ += count * (count + 1) // 2
        
        return summ
