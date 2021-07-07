class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        mxProfit = 0
        for i in range(1,len(prices)):
            mxProfit += max(prices[i]-prices[i-1], 0)
        
        return mxProfit
