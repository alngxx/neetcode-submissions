class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Sliding Window: O(n), O(1) """
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            # if found higher price, update max profit
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)

            # if found lower price, buy it (slide window)
            else:
                l = r
        return max_profit