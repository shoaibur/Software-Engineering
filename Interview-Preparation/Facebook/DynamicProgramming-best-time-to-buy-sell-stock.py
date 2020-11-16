class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        minprice = prices[0]
        maxprofit = 0
        for price in prices[1:]:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit
