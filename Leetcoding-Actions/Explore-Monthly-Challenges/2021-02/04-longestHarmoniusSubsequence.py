class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        T: O(n) and S: O(n)
        '''
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        maxLen = 0
        for key in d:
            if key + 1 in d:
                maxLen = max(maxLen, d[key] + d[key + 1])
        
        return maxLen
