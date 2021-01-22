class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t: return False
        ns, nt = len(s), len(t)
        if abs(ns - nt) > 1: return False
        
        if ns > nt:
            s, t = t, s
            ns, nt = nt, ns
        
        i = 0
        while i < nt:
            charS = s[i] if i < ns else '$'
            charT = t[i]
            if charS != charT:
                # skip charT
                # skip charS and charT
                return s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
            else:
                i += 1
        return False
