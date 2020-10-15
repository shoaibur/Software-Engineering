class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        '''
        T: O(n)
        S: O(1)
        '''
        firstMax = float('-inf')
        secondMax = float('-inf')
        
        for i, num in enumerate(nums):
            if num > firstMax:
                secondMax = firstMax
                firstMax = num
                firstMaxIndex = i
            elif num > secondMax:
                secondMax = num
        
        if firstMax >= 2 * secondMax:
            return firstMaxIndex
        return -1
