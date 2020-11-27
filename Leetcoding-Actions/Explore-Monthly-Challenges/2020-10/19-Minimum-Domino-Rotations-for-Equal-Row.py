class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        Count occurance of each item in A.
        Count occurance of each item in B.
        Count occurance of each item when it's same in both A and B.
        
        We need occurances of one item equal length of A or B, which
        can be computed by adding occurances in A and B and subtracting
        the number of same occurances.
        
        Min rotation is the min of occurances in A and B minus the number
        of same occurances.
        
        T: O(n) and S: O(1)
        '''
        aCount = [0] * 6
        bCount = [0] * 6
        sameCount = [0] * 6
        
        for i in range(len(A)):
            aCount[A[i]-1] += 1
            bCount[B[i]-1] += 1
            
            if A[i] == B[i]:
                sameCount[A[i]-1] += 1
                
        for i in range(6):
            if aCount[i] + bCount[i] - sameCount[i] == len(A):
                return min(aCount[i], bCount[i]) - sameCount[i]
        
        return -1
