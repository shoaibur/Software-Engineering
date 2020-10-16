class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        '''
        T: O(n)
        S: O(n)
        '''
        if len(A) != len(B): return False
        n = len(A)
        
        if A == B:
            seenA = set()
            for i in range(n):
                if A[i] in seenA:
                    return True
                seenA.add(A[i])
            return False
        else:
            iA, iB = [], []
            for i in range(n):
                if A[i] != B[i]:
                    iA.append(A[i])
                    iB.append(B[i])
                    if len(iA) > 2: return False
            if iA != iB[::-1]: return False
            return True
