class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        '''
        T: O(n) and S: O(n)
        '''
        res = list(range(1, n - k))
        for i in range(k + 1):
            if i % 2 == 0:
                res.append(n - k + i // 2)
            else:
                res.append(n - i // 2)
        return res
