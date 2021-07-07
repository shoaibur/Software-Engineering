class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        if len(nums) < 3: return False
        minVal = [nums[0]]
        for num in nums[1:]:
            minVal.append( min(minVal[-1], num) )
        
        stack = [nums[-1]]
        for j in range(len(nums)-2, 0, -1):
            # Condition: nums[i] < nums[k] < nums[j]
            # nums[i] = nums[j - 1]
            # nums[j] = nums[j]
            # nums[k] = stack[-1]
            while stack and stack[-1] < nums[j]: # Check if nums[k] < nums[j]
                if stack[-1] > minVal[j - 1]: # Check if nums[i] < nums[k]
                    return True
                stack.pop()
            stack.append(nums[j])
            
        return False
