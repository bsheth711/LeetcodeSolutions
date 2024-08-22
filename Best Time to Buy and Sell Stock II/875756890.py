class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            cur = prices[i + 1] - prices[i]

            if  cur > 0:
                profit += cur

        return profit