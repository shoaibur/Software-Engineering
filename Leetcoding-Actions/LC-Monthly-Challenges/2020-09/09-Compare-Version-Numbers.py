class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        
        def removeLeadingZeros(s):
            while len(s) > 1 and s[0] == '0':
                s = s[1:]
            return s
        
        ver1 = [removeLeadingZeros(ver1[i]) for i in range(len(ver1))]
        ver2 = [removeLeadingZeros(ver2[i]) for i in range(len(ver2))]
        
        i = 0
        while i < max(len(ver1), len(ver2)):
            v1 = ver1[i] if i < len(ver1) else 0
            v2 = ver2[i] if i < len(ver2) else 0
            i += 1
            if int(v1) > int(v2): return 1
            if int(v1) < int(v2): return -1
        return 0
