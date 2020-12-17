class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        '''
        T: O(n^2) and S: O(n^2)
        '''
        count = 0
        
        abDict = {}
        for a in A:
            for b in B:
                abDict[a + b] = abDict.get(a + b, 0) + 1
        
        cdDict = {}
        for c in C:
            for d in D:
                complement = -(c + d)
                count += abDict.get(complement, 0)
        
        return count
