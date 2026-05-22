class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Greedy: O(n), O(1)
        Day-to-day positive difference: if tomorrow > today, take the profit
        """
        # Edge case: price lower day by day -> never buy, keep profit = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
        