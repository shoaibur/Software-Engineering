class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums: return -2147483648
        
        currSum = nums[0]
        maxSum = nums[0]
        
        for num in nums[1:]:
            currSum = max(currSum+num, num)
            maxSum = max(maxSum, currSum)
            
        return maxSum
