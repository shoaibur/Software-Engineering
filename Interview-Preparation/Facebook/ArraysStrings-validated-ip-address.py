class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.isIPv4(IP): return 'IPv4'
        elif self.isIPv6(IP): return 'IPv6'
        else: return 'Neither'
    
    def isIPv4(self, ip):
        # IPv4: len=4; len of each part=1-3; each part < 255; each part = digits; each part not leading zeros
        ip = ip.split('.')
        if len(ip) != 4: return False
        for t in ip:
            if len(t) < 1 or len(t) > 3: return False
            for char in t:
                if not char.isdigit(): return False
            if t[0] == '0' and len(t) != 1: return False
            if int(t) > 255: return False
        return True
    
    def isIPv6(self, ip):
        # len=8; len of each part=1-4; each part = not hex
        ip = ip.split(':')
        if len(ip) != 8: return False
        for t in ip:
            if len(t) < 1 or len(t) > 4: return False
            for char in t:
                if char not in '0123456789ABCDEFabcdef':
                    return False
        return True
    
