class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        '''
        T: O(n) and S: O(1)
        '''
        return all(abs(i - A[i]) <= 1 for i in range(len(A)))
