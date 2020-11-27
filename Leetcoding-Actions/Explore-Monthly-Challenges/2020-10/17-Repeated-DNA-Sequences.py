class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        T: O(n)
        S: O(n)
        '''
        result = set()
        seqSet = set()
        i, j = 0, 9
        while j < len(s):
            curSeq = s[i:j+1]
            if curSeq in seqSet:
                result.add(curSeq)
            else:
                seqSet.add(curSeq)
            i, j = i + 1, j + 1
            
        return result
