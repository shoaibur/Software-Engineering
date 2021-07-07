class Solution:
    def isHappy(self, n: int) -> bool:
        nSet = set()
        while n > 1:
            if n in nSet: return False
            nSet.add(n)
            k = 0
            while n:
                n, rem = divmod(n, 10)
                k += rem ** 2
            n = k
        return n == 1
