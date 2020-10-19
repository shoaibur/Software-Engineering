class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        T: O(n2 * n1 log n1); can be reduced to O(n2 * n1) by using char counter
        S: O(n1); can be reduced to O(26) = O(1) by using character counting array
        '''
        n1, n2 = len(s1), len(s2)
        s1 = sorted(s1)
        
        for i in range(n2 - n1 + 1):
            if s1 == sorted(s2[i:i+n1]):
                return True
        
        return False
