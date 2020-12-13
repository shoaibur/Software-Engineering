class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [nums[0]] * n
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i]
            
        rightSum = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i]
        
        result = [0] * n
        for i in range(n):
            if i == n - 1:
                result[i] = (i+1)*nums[i] - leftSum[i]
            else:
                result[i] = (i+1)*nums[i] - leftSum[i] + rightSum[i+1] - (n-i-1)*nums[i]
        
        return result
