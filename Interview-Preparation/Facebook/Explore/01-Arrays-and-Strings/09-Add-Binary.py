class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str2num = {'0': 0, '1': 1}
        num2str = {0: '0', 1: '1'}
        result = ''
        na, nb = len(a), len(b)
        i, j, carry = na-1, nb-1, 0
        while i >= 0 or j >=0 or carry:
            va = str2num[a[i]] if i >= 0 else 0
            vb = str2num[b[j]] if j >= 0 else 0
            i, j = i-1, j-1
            summ = va + vb + carry
            carry, s = divmod(summ, 2)
            result += num2str[s]
        return result[::-1]
