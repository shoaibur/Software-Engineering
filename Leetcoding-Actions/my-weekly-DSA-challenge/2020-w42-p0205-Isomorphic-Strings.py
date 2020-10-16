class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        T: O(n)
        S: O(n)
        '''
        if not s and not t: return True
        if not s or not t: return False
        
        isoMap = {}
        seenT = set()
        for i in range(len(s)):
            if s[i] not in isoMap:
                if t[i] in seenT:
                    return False
                isoMap[s[i]] = t[i]
                seenT.add(t[i])
            elif isoMap[s[i]] != t[i]:
                return False
        return True
