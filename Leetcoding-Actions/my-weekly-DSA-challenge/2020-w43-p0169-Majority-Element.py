class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        n = len(nums)
        
        itemCounter = {}
        for num in nums:
            itemCounter[num] = itemCounter.get(num, 0) + 1
            
        for num in itemCounter:
            if itemCounter[num] > n // 2:
                return num
        return
