class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        ns1 = len(s1)
        ns2 = len(s2)
        
        for i in range(ns2 - ns1 + 1):
            if sorted(s2[i:i+ns1]) == s1:
                return True
        return False
        
        '''
        ns1 = len(s1)
        ns2 = len(s2)
        
        countS1 = [0] * 26
        for char in s1:
            idx = ord(char) - ord('a')
            countS1[idx] += 1
        
        for i in range(ns2 - ns1 + 1):
            sub = s2[i:i+ns2]
            countS2 = [0] * 26
            for char in sub:
                idx = ord(char) - ord('a')
                countS2[idx] += 1
                if countS1 == countS2:
                    return True
        return False
        '''
