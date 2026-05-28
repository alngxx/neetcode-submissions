class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0    # If no profit, return 0

        for r in range(1, len(prices)):
            # If found higher prices, calculate profit. Then update max_profit so far
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            # Else if found lower prices, buy that day, slide window
            else:
                l = r
        return max_profit  