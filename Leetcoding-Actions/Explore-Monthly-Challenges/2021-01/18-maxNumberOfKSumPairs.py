class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        operationCount = 0
        d = {}
        for num in nums:
            if d.get(k-num, 0) > 0:
                operationCount += 1
                d[k-num] -= 1
            else:
                d[num] = d.get(num, 0) + 1
        
        return operationCount
