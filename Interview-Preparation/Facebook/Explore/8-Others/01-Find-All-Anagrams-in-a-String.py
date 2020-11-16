class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p = sorted(p)
        ns = len(s)
        np = len(p)
        
        result = []
        
        for i in range(ns-np+1):
            if sorted(s[i:i+np]) == p:
                result.append(i)
        return result
        
        
        '''
        countP = [0] * 26
        for char in p:
            idx = ord(char) - ord('a')
            countP[idx] += 1
        
        np = len(p)
        ns = len(s)
        
        result = []
        
        for i in range(ns-np+1):
            subS = s[i:i+np]
            countS = [0] * 26
            for char in subS:
                idx = ord(char) - ord('a')
                countS[idx] += 1
                if countS == countP:
                    result.append(i)
        return result
        '''
