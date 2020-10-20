class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        Find decreasing order from left.
        Find max of the remaining right. Take right most max if multiple max exist.
        Swap right max with it's immediate smaller one in the left.
        
        9   8   2   3   7   6  1
                    i   max
                    
        T: O(n) and S: O(1)
        '''
        nums = [i for i in str(num)]
        n = len(nums)
        if n <= 1: return num
        
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                break
        if i == n-1 and nums[i-1] >= nums[i]:
            return num
        
        maxRight = nums[i]
        maxRightIndex = i
        for j in range(i+1, n):
            if nums[j] >= maxRight:
                maxRight = nums[j]
                maxRightIndex = j
        
        for j in range(i):
            if nums[j] < maxRight:
                nums[j], nums[maxRightIndex] = nums[maxRightIndex], nums[j]
                break
        
        return int( ''.join(nums) )
