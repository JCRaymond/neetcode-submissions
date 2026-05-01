class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        low_i = 0
        low = prices[low_i]

        best_profit = 0
        for i in range(1, n):
            if prices[i] < low:
                low_i = i
                low = prices[i]
                continue
            
            best_profit = max(best_profit, prices[i] - low)
        
        return best_profit
            
