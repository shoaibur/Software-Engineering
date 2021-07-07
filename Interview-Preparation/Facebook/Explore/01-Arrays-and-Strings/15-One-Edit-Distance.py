class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if not s and len(t) == 1: return True
        if not t and len(s) == 1: return True
        if s == t: return False
        
        ns, nt = len(s), len(t)
        if abs(ns-nt) > 1: return False
        
        for i in range(min(ns, nt)):
            if s[i] != t[i]:
                return s[i:] == t[i+1:] or s[i+1:] == t[i:] or s[i+1:] == t[i+1:]
        if i+1 == min(ns, nt) and abs(ns-nt) == 1: return True
        return False
