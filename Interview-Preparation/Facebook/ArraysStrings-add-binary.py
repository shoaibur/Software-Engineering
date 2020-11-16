class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Solution 1
        # a = int(a, 2)
        # b = int(b, 2)
        # c = a + b
        # return str(bin(c))[2:]
        
        # Solution 2
        result = []
        
        na, nb = len(a), len(b)
        i, j, carry = len(a)-1, len(b)-1, 0
        
        while i >= 0 or j >= 0 or carry:
            va = int(a[i]) if i >= 0 else 0
            vb = int(b[j]) if j >= 0 else 0
            sums = va + vb + carry
            # s, carry = sums % 2, sums // 2
            carry, s = divmod(sums, 2)
            result.append(str(s))
            i -= 1
            j -= 1
            
        return ''.join(result[::-1])
