class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit
