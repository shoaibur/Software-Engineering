class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price-minPrice)
        
        return maxProfit
