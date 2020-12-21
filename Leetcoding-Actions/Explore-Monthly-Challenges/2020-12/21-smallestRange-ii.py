class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        '''
        T: O(n log n) and S: O(1)
        '''
        A.sort()
        mn, mx = A[0], A[-1]
        smallestDiff = mx - mn
        
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            possibleMax = max(mx - K, A[i] + K)
            possibleMin = min(mn + K, A[i+1] - K)
            smallestDiff = min(smallestDiff, possibleMax - possibleMin)
            
        return smallestDiff
