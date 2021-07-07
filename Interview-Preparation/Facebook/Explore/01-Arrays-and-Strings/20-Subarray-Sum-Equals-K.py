class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        1 1 1
        1 2 3
        cumSum - k = value
        '''
        currSum = 0
        count = 0
        
        d = {}
        
        for num in nums:
            currSum += num
            if currSum == k:
                count += 1
            if currSum - k in d:
                count += d[currSum-k]
            d[num] = d.get(num, 0) + 1
        return count
