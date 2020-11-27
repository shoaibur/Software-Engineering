class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        if not A or not B: return 0
        
        def shiftANDoverlap(A, B):
            overlapCount = 0
            n = len(A)
            # Shift
            for x in range(n):
                for y in range(n):
                    tempCount = 0
                    # Overlap
                    for i in range(y, n):
                        for j in range(x, n):
                            if A[i][j] == 1 and B[i-y][j-x] == 1:
                                tempCount += 1
                    overlapCount = max(overlapCount, tempCount)
            return overlapCount
        
        return max( shiftANDoverlap(A, B), shiftANDoverlap(B, A) )
