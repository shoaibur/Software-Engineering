# Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal 
# numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;
# Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.
# IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 
# 16 bits. The groups are separated by colons (":"). 
# For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit 
# some leading zeros among four hexadecimal digits and some low-case characters in the address to 
# upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros 
# and using upper cases).
# However, we don't replace a consecutive group of zero value with a single empty group using two consecutive 
# colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
# Besides, extra leading zeros in the IPv6 is also invalid. 
# For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
# Note: You may assume there is no extra space or special characters in the input string.

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
