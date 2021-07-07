class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        sum = n * k + rem
        '''
        summ = 0
        d = {0: -1}
        for i, num in enumerate(nums):
            summ += num
            if k != 0:
                summ = summ % k
            if summ in d:
                if (i - d[summ]) >= 2:
                    return True
            else:
                d[summ] = i
        return False
