class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        T: O(n) and S: O(n)
        '''
        n = len(nums)
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        missing, twice = None, None
        for num in range(1, n+1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                twice = num
            
            if missing and twice:
                return [twice, missing]
