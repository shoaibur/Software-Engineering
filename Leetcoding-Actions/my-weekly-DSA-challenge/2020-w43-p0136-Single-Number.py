class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Solution 1: T: O(n) and O(n)
        '''
        # counter = {}
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1
        # for num in counter:
        #     if counter[num] == 1:
        #         return num
        # return
    
        '''
        Solution 2:
        a xor b xor a = b --> unique is b
        T: O(n) ans S: O(1)
        '''
        a = 0 # a xor 0 = a
        for i in range(len(nums)):
            a = a ^ nums[i]
        return a
