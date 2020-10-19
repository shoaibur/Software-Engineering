class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        1, 7, 3, 6, 5, 6
        0  1  8  11 17 22
                 11 6   0
        T: O(n) and S: O(n)
        '''
        n = len(nums)
        if n < 3: return -1
        
        leftSum = [0] * n
        rightSum = [0] * n
        
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        
        for i in range(n):
            if leftSum[i] == rightSum[i]:
                return i
        
        return -1
