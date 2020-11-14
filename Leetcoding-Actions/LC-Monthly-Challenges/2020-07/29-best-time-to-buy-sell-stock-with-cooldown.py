class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Case 1: Have a stock on day i
          -Case 1a: Carried from previous day i-1
            
          -Case 1b: Bought on day i
             
        Case 2: Have no stock on day i
          -Case 2a: Sold on day i
             sold[i] = held[i-1] + prices[i]
             
          -Case 2b: Moving forward from cooldown, do nothing
             
        '''
        
        sold, held, reset = float('-inf'), float('-inf'), 0
        
        for price in prices:
            sold, held, reset = held + price, max(held, reset-price), max(reset, sold)
        return max(sold, reset)
