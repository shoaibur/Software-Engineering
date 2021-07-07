class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        A.sort()
        maxSum = -1
        i, j = 0, len(A) - 1
        while i < j:
            add = A[i] + A[j]
            if add < K:
                maxSum = max(maxSum, add)
                i += 1
            else:
                j -= 1
        return maxSum
