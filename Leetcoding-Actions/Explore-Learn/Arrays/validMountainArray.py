class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        '''
        T: O(log n + n) and S: O(1)
        '''
        def binarySearch(A):
            lo, hi = 0, len(A) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if A[mid] > A[mid + 1]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        i = binarySearch(A)
        if (i == 0 or i == len(A)-1):
            return False
        for j in range(i+1, len(A)):
            if A[j-1] <= A[j]:
                return False
        for j in range(i-1, -1, -1):
            if A[j + 1] <= A[j]:
                return False
        
        return True
