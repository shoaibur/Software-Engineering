class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
        maxSum = -2
        currSum = -2
        1-> currSum = max(currSum+currNum, currNum)
            maxSum = max(maxSum, currSum)
        
        T: O(n) and S: O(1)
        '''
        maxSum = nums[0]
        currSum = nums[0]
        
        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
            
        return maxSum
