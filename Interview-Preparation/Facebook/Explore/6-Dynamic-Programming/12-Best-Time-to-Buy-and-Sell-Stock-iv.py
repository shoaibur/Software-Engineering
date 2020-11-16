class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        tk_cost = [float(inf)] * k
        tk_profit = [0] * k
        
        for price in prices:
            for i in range(k):
                if i == 0:
                    tk_cost[i] = min(tk_cost[i], price)
                else:
                    tk_cost[i] = min(tk_cost[i], price - tk_profit[i-1])
                
                tk_profit[i] = max(tk_profit[i], price - tk_cost[i])
        
        return tk_profit[-1]
