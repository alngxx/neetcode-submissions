class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0    # If no profit, return 0

        for r in range(1, len(prices)):
            # if there is profit, keep expanding window
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)   # update max profit so far
            
            # else, slide window
            else:
                l = r
        
        return max_profit
        
        

        

        