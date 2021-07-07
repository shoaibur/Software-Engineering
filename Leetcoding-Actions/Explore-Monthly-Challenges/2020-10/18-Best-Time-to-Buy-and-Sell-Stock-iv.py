class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        prices =        [3, 2, 6, 5, 0, 3]
        profit @ k = 0:  0  0  0  0  0  0
                 k = 1:  0  0  4  4  4  4
                 k = 2:  0  0  4  4  4  7
        
        On a given day, we may have two cases: keep stock or sell stock
        If kept:
        profit is profit of previous day, i.e. d-1
        
        If sold:
        profit is prices[d] + profit at previous trasaction - price at that transaction.
        
        The previous transaction could be on any day before d. So,
        
        profit[t][d] = prices[d] + max( profit[t-1][x] - prices[x] )
        
        where, x ranges from 0 to d-1.
        Computations in second part is redundant; avoid this by keep tracking for each x as:
        
        curMaxProfit = max( profit[t-1][d-1] - prices[d-1]
        
        T: O(nk) and S: O(nk)
        '''
        if len(prices) <= 1: return 0
        
        if k >= len(prices)//2:
            return sum([i - j for i,j in zip(prices[1:],prices[:-1]) if i-j>0])
        
        profit = [[0 for d in prices] for t in range(k+1)]
        
        for t in range(1, k+1):
            curMaxProfit = float('-inf')
            for d in range(1, len(prices)):
                curMaxProfit = max(curMaxProfit, profit[t-1][d-1] - prices[d-1])
                profit[t][d] = max(profit[t][d-1], prices[d] + curMaxProfit)
                
        return profit[-1][-1]
