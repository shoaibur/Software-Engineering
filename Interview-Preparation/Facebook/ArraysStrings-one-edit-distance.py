class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t: return False
        ns, nt = len(s), len(t)
        if ns > nt:
            ns, nt = nt, ns
            s, t = t, s
        if nt - ns > 1: return False
        
        if ns == nt:
            firstDisparity = False
            i, j = 0, 0
            while i < ns:
                if s[i] != t[j]:
                    if firstDisparity:
                        return False
                    else:
                        firstDisparity = True
                i, j = i+1, j+1
        else:
            firstDisparity = False
            i, j = 0, 0
            while i < ns:
                if s[i] != t[j]:
                    if firstDisparity:
                        return False
                    else:
                        firstDisparity = True
                        j += 1
                else:
                    i, j = i+1, j+1
        return True
